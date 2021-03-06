from datetime import datetime
from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from app.models.MyUser import MyUser

from app.mserializers.QuestionSerializer import QuestionCreateSerializer, QuestionSerializer, QuestionSubmitAnswerSerializer, QuestionVoteSerializer, QuestionWithoutRAnswerSerializer
from app.models.Question import Question
from app.utils.paginations import SmallResultsSetPagination


class QuestionApi(generics.ListCreateAPIView):
    """
    List questions.
    """
    serializer_class = QuestionSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Question.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.id
        serializer = QuestionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a question.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRandom(generics.ListAPIView):
    """
    List questions.
    """
    serializer_class = QuestionWithoutRAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        randomQuestion = Question.objects.order_by('?')
        return randomQuestion


class QuestionUpvote(generics.UpdateAPIView):
    """
    Retrieve a question.
    """
    queryset = Question.objects.all()

    def patch(self, request, *args, **kwargs):
        question = self.get_object()
        if request.user in question.upvote.all():
            question.upvote.remove(request.user.id)
            question.n_upvote -= 1
            question.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Upvote removed", "n_upvote": question.n_upvote})
        else:
            question.upvote.add(request.user.id)
            question.n_upvote += 1
            question.save()
            return Response(status=status.HTTP_200_OK, data={"message": "Upvote added", "n_upvote": question.n_upvote})


class QuestionDownvote(generics.UpdateAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        question = self.get_object()
        if request.user in question.downvote.all():
            question.downvote.remove(request.user.id)
            question.n_downvote -= 1
            question.save()
            return Response(status=status.HTTP_200_OK, data={"message": "downvote removed", "n_downvote": question.n_downvote})
        else:
            question.downvote.add(request.user.id)
            question.n_downvote += 1
            question.save()
            return Response(status=status.HTTP_200_OK, data={"message": "downvote added", "n_downvote": question.n_downvote})
        

class QuestionSubmitAnswer(generics.GenericAPIView):
    queryset = Question.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuestionSubmitAnswerSerializer
    
    def post(self, request, *args, **kwargs):
        question = self.get_object()
        right_answer = question.right_answer
        answer = request.data['answer']
        is_right = answer == right_answer
        
        user = MyUser.objects.get(id=request.user.id)
        # Update the user's total exp
        if is_right:
            user.learn_progress.total_exp += question.exp
            
        # Update the user's streak
        date = datetime.now().strftime("%Y-%m-%d")
        lastest7dayexp = user.learn_progress.lastest7dayexp
        lastest7dayexp = lastest7dayexp if lastest7dayexp else {}
        if not date in lastest7dayexp:
            user.learn_progress.streak_count+=1
        # datetime now timestamp
        lastest7dayexp[date] = user.learn_progress.total_exp
        user.learn_progress.lastest7dayexp = lastest7dayexp
        # Update user's learn progress
        user.learn_progress.save()
        
        return Response(status=status.HTTP_200_OK, data={\
                "exp": question.exp,
                "is_right": is_right,
                "lastest7dayexp": user.learn_progress.lastest7dayexp,
                "message": "Answer submitted",
                "streak_count": user.learn_progress.streak_count,
                "total_exp": user.learn_progress.total_exp,
            })
        
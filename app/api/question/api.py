from datetime import datetime, timedelta
from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from app.models.MyUser import MyUser

from app.mserializers.QuestionSerializer import QuestionCreateSerializer, QuestionSerializer, QuestionSubmitAnswerSerializer, QuestionVoteSerializer, QuestionWithoutRAnswerSerializer
from app.models.Question import QUESTION_TYPE_CHOICES, Question
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


class QuestionRandom(generics.GenericAPIView):
    """
    List questions.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        questions = Question.objects.order_by('?')
        questions = questions[:1]
        question = questions[0]
        
        kwargs.setdefault('context', {})['request'] = request
        serializer = QuestionWithoutRAnswerSerializer(question, **kwargs)
        return Response(serializer.data)
        


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
    ftime = "%Y-%m-%d"
    
    def format_time(self, time):
        return time.strftime(self.ftime)
    
    def validate_token(self, token: str, question: Question, user, **kwargs):
        tokens = token.split("ptoken")
        token_user_id = tokens[0]
        token_time = tokens[1]
        
        if token_user_id != str(user.id):
            return False
        else:
            if datetime.now() - datetime.strptime(token_time, "%Y%m%d%H%M%S") > timedelta(seconds=question.time_limit+10):
                return False
            else:
                return True
        
        
    
    def post(self, request, *args, **kwargs):
        question = self.get_object()
        right_answer = question.right_answer
        answer = request.data['answer']
        token = request.data['token']
        user = request.user
        is_valid = self.validate_token(token, question, user, **kwargs)
        if not is_valid:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid token"})
        is_right = answer == right_answer
        
        user = MyUser.objects.get(id=request.user.id)
        # Update the user's total exp
        if is_right:
            user.learn_progress.total_exp += question.exp
            
        # Update the user's streak
        date = self.format_time(datetime.now())
        lastest7dayexp = user.learn_progress.lastest7dayexp
        lastest7dayexp = lastest7dayexp if lastest7dayexp else {}
                
        if not date in lastest7dayexp:
            #  clean the lastest7dayexp
            for key in list(lastest7dayexp):
                if datetime.strptime(key, self.ftime) < datetime.now() - timedelta(days=7):
                    lastest7dayexp.pop(key)
            # if yesterday answer is right, add 1 to the streak
            yesterday = datetime.now() - timedelta(days=1)
            is_streak = self.format_time(yesterday) in lastest7dayexp
            user.learn_progress.streak_count+=1 if is_streak else 1
            # update exp today
            lastest7dayexp[date] = question.exp
        else:
            # update exp today
            if is_right:
                lastest7dayexp[date] += question.exp
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
                "today_exp": lastest7dayexp[date]
            })

class QuestionTypeApi(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        question_types = []
        for question_type_choice in QUESTION_TYPE_CHOICES:
          question_type = {}
          question_type['abbr'] = question_type_choice[0]
          question_type['name'] = question_type_choice[1]
          question_types.append(question_type)
        return Response(status=status.HTTP_200_OK, data=question_types)
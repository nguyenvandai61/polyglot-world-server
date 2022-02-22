from rest_framework import generics, mixins, serializers, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import LimitOffsetPagination
from app.models.Comment import Comment

from app.models.Post import Post
from app.mserializers.CommentSerializers import CommentCreateResponseSerializer, CommentCreateSerializer, CommentSerializer, CommentVoteResponseSerializer, CommentVoteSerializer
from app.mserializers.UserSerialziers import ProfileGeneralSerializer
from app.utils.paginations import SmallResultsSetPagination

from drf_yasg.utils import swagger_auto_schema

class PostComment(mixins.DestroyModelMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super().get_queryset()\
            .filter(post_id=self.kwargs['pk']).filter(parent_comment=None).order_by('time_stamp')
    
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if (self.request.query_params.get('limit') or self.request.query_params.get('offset')):
            self.pagination_class = LimitOffsetPagination
        return self.paginator.paginate_queryset(queryset, self.request, view=self)  
    
    @swagger_auto_schema(
        request_body=CommentCreateSerializer,
        responses={
            200: CommentCreateResponseSerializer,
        }        
    )
    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        comment_id = self.kwargs.get('comment_id')
        content = request.data['content']
        if content == "":
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Comment is empty"})

        try:
            post = Post.objects.get(id=post_id)
            comment_parent = Comment.objects.get(id=comment_id) if comment_id else None
            comment = Comment().create(author=request.user, content=content, post=post, parent=comment_parent)
            post.comments.add(comment)
            post.n_comment += 1
            serializer = CommentCreateResponseSerializer(comment)
            post.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
    
    def delete(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        comment_id = self.kwargs['comment_id']
        try:
            comment = Comment.objects.get(id=comment_id)
            post = Post.objects.get(id=post_id)
            post.comments.remove(comment)
            post.n_comment -= 1
            post.save()
            comment.delete()
            return Response(status=status.HTTP_200_OK, data={"detail": "Comment deleted"})
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Comment not found"})
        
        
class PostCommentVote(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentVoteSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['comment_id'])

    @swagger_auto_schema(responses={200: CommentVoteResponseSerializer})
    def put(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        comment_id = self.kwargs['comment_id']
        vote = request.data['vote']
        
        comment = Comment.objects.get(id=comment_id)
        post = Post.objects.get(id=post_id)
        has_upvoted = comment.upvotes.filter(id=request.user.id).exists()
        has_downvoted = comment.downvotes.filter(id=request.user.id).exists()
        
        if has_upvoted:
            if not vote == 1:
                comment.upvotes.remove(request.user)
                comment.n_upvote -= 1
            if vote == -1:
                comment.downvotes.add(request.user)
                comment.n_downvote += 1
        elif has_downvoted:
            if not vote == -1:
                comment.downvotes.remove(request.user)
                comment.n_downvote -= 1
            if vote == 1:
                comment.upvotes.add(request.user)
                comment.n_upvote += 1
        else:
            if vote == 1:
                comment.upvotes.add(request.user)
                comment.n_upvote += 1
            elif vote == -1:
                comment.downvotes.add(request.user)
                comment.n_downvote += 1
        
        serializer = CommentVoteResponseSerializer(comment)
        comment.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
from rest_framework import generics, mixins, serializers, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import LimitOffsetPagination
from app.models.Comment import Comment

from app.models.Post import Post
from app.mserializers.CommentSerializers import CommentCreateSerializer, CommentSerializer
from app.mserializers.UserSerialziers import ProfileGeneralSerializer
from app.utils.paginations import SmallResultsSetPagination


class PostComment(mixins.DestroyModelMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['pk'])
    
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if (self.request.query_params.get('limit') or self.request.query_params.get('offset')):
            self.pagination_class = LimitOffsetPagination
        return self.paginator.paginate_queryset(queryset, self.request, view=self)  
    
    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        content = request.data['content']
        if content == "":
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Comment is empty"})

        try:
            post = Post.objects.get(id=post_id)
            comment = Comment().create(author=request.user, content=content, post=post)
            post.comments.add(comment)
            post.n_comment += 1
            serializer = CommentCreateSerializer(comment)
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
        
        
class PostChildComment(mixins.DestroyModelMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(parent_id=self.kwargs['comment_id'])    

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        comment_id = self.kwargs['comment_id']
        content = request.data['content']
        if content == "":
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Comment is empty"})

        try:
            parent_comment = Comment.objects.get(id=comment_id)
            post = Post.objects.get(id=post_id)
            comment = Comment().create(author=request.user, content=content, post=post, parent=parent_comment)
            parent_comment.child_comments.add(comment)
            parent_comment.save()
            return Response(status=status.HTTP_200_OK, data={
                "id": comment.id,
                "author_id": comment.author.id,
                "parent_id": comment.parent_comments.id,
                "time_stamp": comment.time_stamp,
                "content": comment.content,
                "detail": "Comment created"
            })
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Comment not found"})
    
    def delete(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        comment_id = self.kwargs['comment_id']
        try:
            comment = Comment.objects.get(id=comment_id)
            post = Post.objects.get(id=post_id)
            post.child_comments.remove(comment)
            post.child_comments.n_comment -= 1
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
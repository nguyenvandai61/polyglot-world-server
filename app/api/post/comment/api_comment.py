from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.models.Comment import Comment

from app.models.Post import Post
from app.mserializers.CommentSerializers import CommentSerializer
from app.utils.paginations import SmallResultsSetPagination


class PostComment(mixins.DestroyModelMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['pk'])    

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
            post.save()
            return Response(status=status.HTTP_200_OK, data={
                "id": comment.id,
                "author_id": comment.author.id,
                "content": comment.content,
                "detail": "Comment created"
            })
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
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.models.Comment import Comment

from app.models.Post import Post


class PostHeart(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        is_heart = request.data['is_heart']
        try:
            post = Post.objects.get(id=post_id)
            current_state = post.hearts.filter(id=request.user.id).exists()
            if current_state == is_heart:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Post heart state is already {}".format(is_heart)})
            post.n_heart += 1 if is_heart else -1
            post.save()
            if is_heart:
                post.hearts.add(request.user)
                return Response(status=status.HTTP_200_OK, data={"is_heart": True, "detail": "Post hearted"})
            else:
                post.hearts.remove(request.user)
                return Response(status=status.HTTP_200_OK, data={"is_heart": False, "detail": "Post unhearted"})
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})


class PostComment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        content = request.data['content']
        if content == "":
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Comment is empty"})

        try:
            comment = Comment().create(author=request.user, content=content)
            post = Post.objects.get(id=post_id)
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
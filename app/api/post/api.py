from rest_framework import generics, serializers, status
from rest_framework.response import Response

from app.mserializers import PostSerializers
from app.models.Post import Post


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()
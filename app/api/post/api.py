from rest_framework import generics, serializers, status
from rest_framework.response import Response

from app.mserializers.PostSerializers import PostSerializer
from app.models.Post import Post
from app.models.Language import Language


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        data["author"] = request.user.id
        data['language'] = Language.objects.get(code=request.data['lang_code']).id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
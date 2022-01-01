from rest_framework import generics, status
from rest_framework.response import Response
from app.models.MyUser import MyUser

from app.mserializers.PostSerializers import PostCreateSerializer, PostSerializer
from app.models.Post import Post
from app.models.Language import Language
from app.mserializers.UserSerialziers import ProfileGeneralSerializer
from app.utils.paginations import SmallResultsSetPagination


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = SmallResultsSetPagination

    def create(self, request, *args, **kwargs):
        data = request.data
        author_id = request.user.id
        data["author"] = author_id
        data['language'] = Language.objects.get(
            code=request.data['lang_code']).id
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_object(self):
        try:
            return Post.objects.get(id=self.kwargs['pk'])
        except Post.DoesNotExist:
            return None

    def update(self, request, *args, **kwargs):
        if self.get_object() is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
        serializers = PostSerializer(
            self.get_object(), data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        if self.get_object() is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Post not found'})
        serializers=PostSerializer(self.get_object())
        return Response(serializers.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        if self.get_object() is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Post not found"})
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"detail": "Post deleted"})


class PostListByUser(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        queryset = self.queryset.filter(author=self.kwargs['pk'])
        return queryset
    

class PostListByLanguage(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        lang_id = Language.objects.get(code=self.kwargs['code'])
        queryset = self.queryset.filter(language=lang_id)
        return queryset
    

class PostListByLanguageAndUser(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        lang_id = Language.objects.get(code=self.kwargs['code'])
        queryset = self.queryset.filter(language=lang_id, author=self.kwargs['pk'])
        return queryset
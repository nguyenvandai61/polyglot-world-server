from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from app import serializers

from app.models.Post import Post
from app.mserializers.PostSerializers import HeartSerializer
from app.mserializers.UserSerialziers import ProfileGeneralSerializer
from app.utils.paginations import SmallResultsSetPagination


class PostHeart(generics.ListAPIView, APIView):
    serializer_class = ProfileGeneralSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        return Post.objects.get(id=self.kwargs['pk']).hearts.all()
    
    @swagger_auto_schema(
        request_body=HeartSerializer,
        responses={
            status.HTTP_200_OK: HeartSerializer(many=True),
            status.HTTP_400_BAD_REQUEST: HeartSerializer(many=True),
        }
    )
    def put(self, request, *args, **kwargs):
        post_id = self.kwargs['pk']
        is_hearted = self.request.data['is_hearted']
        
        post = Post.objects.get(id=post_id)
        if is_hearted:
            post.hearts.add(request.user)
            post.n_heart += 1
        else:
            post.hearts.remove(request.user)
            post.n_heart -= 1
        post.save()
        serializer = HeartSerializer({'is_hearted': is_hearted})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

        

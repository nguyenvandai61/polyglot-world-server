from app.models.MyUser import MyUser
from rest_framework import generics, serializers, status, permissions
from rest_framework.response import Response
from app.mserializers.UserSerialziers import FriendExpSerializer, ProfileSerializer, UserSearchFollowSerializer, UserLearnProgressSerializer
from app.models.LearnProgress import LearnProgress
import cloudinary.uploader

from app.utils.paginations import SmallResultsSetPagination, UltraSmallResultsSetPagination


class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve a profile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        user = MyUser.objects.get(id=id)
        return user


class AvatarUpload(generics.UpdateAPIView):
    """
    Upload avatar.
    """
    def get_object(self):
        user_id = self.kwargs.get('id')
        user = MyUser.objects.get(id=user_id)
        return user

    def get_serializer(self, *args, **kwargs):
        pass
    
    def update(self, request, *args, **kwargs):
        user_id = self.kwargs.get('id')
        if user_id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN, data={
                'status': 'error',
                'detail': 'You are not allowed to change this user.'
            })

        avatar = request.data.get('avatar')
        folder = 'avatars/'+str(user_id)
        # Upload image to cloudinary
        cloudImage = cloudinary.uploader.upload(
            avatar,
            folder="polyglot-world/"+folder,
            overwrite=True,
            resource_type="image"
        )
        # Update user avatar
        user = self.get_object()
        user.avatar = cloudImage['url']
        user.save()
        return Response(status=status.HTTP_200_OK, data={
            'status': 'success',
            'detail': 'Avatar updated.',
            'avatar': user.avatar
        })


class UserLearnProgress(generics.GenericAPIView):
    serializer_class = UserLearnProgressSerializer
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get('id')
        user = MyUser.objects.get(id=user_id)
        serializer = self.get_serializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    

class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [permissions.IsAuthenticated]

class FollowUser(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user_id = self.kwargs.get('id')
        if user_id == request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN, data={
                'status': 'error',
                'detail': 'You cannot follow yourself.'
            })
        user = MyUser.objects.get(id=user_id)
            
        # check request url contain unfollow
        if 'unfollow' in request.path:
            user.followers.remove(request.user)
            user.save()
            return Response(status=status.HTTP_200_OK, data={
                'status': 'success',
                'detail': 'You are no longer following this user.'
            })
        else:
            user.followers.add(request.user)
            user.save()
            return Response(status=status.HTTP_200_OK, data={
                'status': 'success',
                'detail': 'You are now following this user.'
            })
            
class UserSearchByUsername(generics.ListAPIView):
    serializer_class = ProfileSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        username = self.kwargs.get('username_query')
        return MyUser.objects.filter(username__icontains=username)
    
class UserSearchFollow(generics.ListAPIView):
    serializer_class = UserSearchFollowSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        username = self.kwargs.get('username_query')
        return MyUser.objects.filter(username__icontains=username)\
            .exclude(id=self.request.user.id).order_by('username')
            
class MyFriendListWithExp(generics.ListAPIView):
    serializer_class = FriendExpSerializer
    pagination_class = SmallResultsSetPagination
    
    def get_queryset(self):
        return MyUser.objects.filter(followers=self.request.user)
    
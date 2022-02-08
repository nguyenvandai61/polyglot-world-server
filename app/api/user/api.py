from app.models.MyUser import MyUser
from rest_framework import generics, serializers, status, permissions
from rest_framework.response import Response
from app.mserializers.UserSerialziers import ProfileSerializer, UserLearnProgressSerializer
from app.models.LearnProgress import LearnProgress
import cloudinary.uploader

from app.utils.paginations import SmallResultsSetPagination


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
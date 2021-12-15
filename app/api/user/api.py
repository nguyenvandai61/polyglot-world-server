from app.models.MyUser import MyUser
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from app.mserializers.UserSerialziers import ProfileSerializer
from app.models.LearnProgress import LearnProgress
import cloudinary.uploader


class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve a profile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        user_id = self.kwargs.get('id')
        user = MyUser.objects.get(id=user_id)
        return user


class AvatarUpload(generics.UpdateAPIView):
    """
    Upload avatar.
    """

    def update(self, request, *args, **kwargs):
        if request.user is None or request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'status': 'failed',
                'detail': 'Authentication credentials were not provided.'})
        user_id = request.user.id
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
        user = request.user
        user.avatar = cloudImage['url']
        user.save()
        return Response(status=status.HTTP_200_OK, data={
            'status': 'success',
            'detail': 'Avatar updated.',
            'avatar': user.avatar
        })

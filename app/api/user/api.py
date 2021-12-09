from app.models.MyUser import MyUser
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from app.mserializers.UserSerialziers import ProfileSerializer
from app.models.LearnProgress import LearnProgress

class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve a profile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        user_id = self.kwargs.get('id')
        user = MyUser.objects.get(id=user_id)
        return user
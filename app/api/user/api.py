from app.models.MyUser import MyUser
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from app.mserializers.UserSerialziers import ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    """
    Retrieve a profile.
    """
    serializer_class = ProfileSerializer

    def get_object(self):
        user_id = self.kwargs.get('id')
        return MyUser.objects.get(id=user_id)
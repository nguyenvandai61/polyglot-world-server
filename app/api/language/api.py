from rest_framework import generics, serializers, status
from rest_framework.response import Response

from app.mserializers import LanguageSerializer
from app.models.Language import Language


class LanguageList(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
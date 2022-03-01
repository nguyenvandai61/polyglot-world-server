from h11 import Response
from rest_framework import generics
from rest_framework.response import Response
from .english_handler import EnglishTranslator



class EnglishTranslateApi(generics.GenericAPIView):
		EnglishTranslator = EnglishTranslator()
		
		def get(self, request, *args, **kwargs):
				word = kwargs['word']
				results = self.EnglishTranslator.translate(word)
				return Response({'results': results})
		
  
from rest_framework import generics
from rest_framework.response import Response

from app.models.Post import Post
from app.models.Comment import Comment
from app.models.Language import Language
from app.models.MyUser import MyUser
from app.models.Question import Question


class StatasticGeneral(generics.GenericAPIView):
		"""
		Statastic general
		"""
		def get(self, request, *args, **kwargs):
				"""
				Get Statastic general
				"""
				postCount = Post.objects.all().count()
				userCount = MyUser.objects.all().count()
				languageCount = Language.objects.all().count()
				commentCount = Comment.objects.all().count()
				questionCount = Question.objects.all().count()
				
				return Response({
					'posts': postCount,
					'users': userCount,
					'languages': languageCount,
					'comments': commentCount,
					'questions': questionCount
				})
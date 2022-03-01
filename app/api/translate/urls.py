from django.urls import path
from .api import EnglishTranslateApi


urlpatterns = [
		path('en/<str:word>', EnglishTranslateApi.as_view(), name='en_translate'),
]

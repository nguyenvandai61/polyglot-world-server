from django.urls import path
from .api import PredictNextWordDict, GetWordDict

urlpatterns = [
	path('nextword/<str:last_word>', PredictNextWordDict.as_view(), name='index'),
	path('word/<str:substart_word>', GetWordDict.as_view(), name='index'),
]

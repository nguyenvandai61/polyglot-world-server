from django.urls import path
from .api import PredictNextWordDict, GetWordDict, PredictLanguageApi

urlpatterns = [
	path('nextword/<str:last_word>', PredictNextWordDict.as_view(), name='predict_next_word_dict'),
	path('word/<str:substart_word>', GetWordDict.as_view(), name='get_word_in_dict'),
  path('language/', PredictLanguageApi.as_view(), name='predict_language'),
]

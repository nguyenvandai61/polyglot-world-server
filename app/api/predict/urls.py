from django.urls import path
from .api import PredictNextWordDict

urlpatterns = [
	path('nextword/<str:last_word>', PredictNextWordDict.as_view(), name='index'),
]

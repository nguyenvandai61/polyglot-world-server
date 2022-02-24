from django.urls import path
from .api import StatasticGeneral

urlpatterns = [
		path('', StatasticGeneral.as_view(), name='index'),
]

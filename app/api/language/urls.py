from django.urls import include, path
from .api import LanguageList


urlpatterns = [
    path('', LanguageList.as_view(), name='language-list'),
]
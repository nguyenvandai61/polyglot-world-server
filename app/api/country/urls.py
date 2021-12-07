from django.urls import include, path
from .api import CountryList


urlpatterns = [
    path('', CountryList.as_view(), name='country-list'),
]
from django.urls import include, path
from .api import ProfileDetail


urlpatterns = [
    path('profile_detail/<int:id>', ProfileDetail.as_view(), name='profile_detail'),
]
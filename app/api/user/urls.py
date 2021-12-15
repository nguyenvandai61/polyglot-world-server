from django.urls import include, path
from .api import ProfileDetail, AvatarUpload


urlpatterns = [
    path('profile_detail/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile_detail/avatar/', AvatarUpload.as_view(), name='avatar_upload'), 
]
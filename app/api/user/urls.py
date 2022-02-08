from django.urls import include, path
from .api import ProfileDetail, AvatarUpload, UserLearnProgress


urlpatterns = [
    path('profile_detail/<int:id>', ProfileDetail.as_view(), name='profile_detail'),
    path('profile_detail/<int:id>/avatar/', AvatarUpload.as_view(), name='avatar_upload'), 
    path('profile_detail/<int:id>/learn_progress/', UserLearnProgress.as_view(), name='learn_progress'),
]
from django.urls import include, path
from .api import PostList


urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
]
from django.urls import include, path
from .api import PostList, PostInfo


urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostInfo.as_view(), name='post-list'),
]
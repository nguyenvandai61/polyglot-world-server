from django.urls import include, path
from .api import PostList, PostInfo


urlpatterns = [
    # path('<int:pk>/', PostList.as_view(), name='post-list'),
    path('', PostList.as_view(), name='post-list'),
]
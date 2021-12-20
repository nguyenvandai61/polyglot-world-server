from django.urls import include, path
from .api import PostList, PostInfo, PostListByUser, PostListByLanguage, PostListByLanguageAndUser


urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostInfo.as_view(), name='post-list'),
    path('user/<int:pk>/', PostListByUser.as_view(), name='post-list-by-user'),
    path('lang/<str:code>/', PostListByLanguage.as_view(), name='post-list-by-language'),
    path('lang/<str:code>/user/<int:pk>/', PostListByLanguageAndUser.as_view(), name='post-list-by-language-and-user'),
]
from django.urls import include, path
from .api import PostList, PostInfo, PostListByUser, PostListByLanguage, PostListByLanguageAndUser
from .heart.api_heart import PostHeart
from .comment.api_comment import PostComment, PostCommentVote

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostInfo.as_view(), name='post-list'),
    path('user/<int:pk>/', PostListByUser.as_view(), name='post-list-by-user'),
    path('lang/<str:code>/', PostListByLanguage.as_view(), name='post-list-by-language'),
    path('lang/<str:code>/user/<int:pk>/', PostListByLanguageAndUser.as_view(), name='post-list-by-language-and-user'),
    
    # Actions
    path('<int:pk>/heart/', PostHeart.as_view(), name='post-like'),
    path('<int:pk>/comment/', PostComment.as_view(), name='post-comment'),
    path('<int:pk>/comment/<int:comment_id>/', PostComment.as_view(), name='post-comment'),
    path('<int:pk>/comment/<int:comment_id>/vote/', PostCommentVote.as_view(), name='post-comment-vote'),
]
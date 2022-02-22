from django.urls import include, path
from .api import ProfileDetail, AvatarUpload, UserLearnProgress, UserList, FollowUser, UserSearchByUsername\
    , UserSearchFollow, MyFriendListWithExp


urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('profile_detail/<int:id>', ProfileDetail.as_view(), name='profile_detail'),
    path('profile_detail/<int:id>/avatar/', AvatarUpload.as_view(), name='avatar_upload'), 
    path('profile_detail/<int:id>/learn_progress/', UserLearnProgress.as_view(), name='learn_progress'),
    path('follow/<int:id>/', FollowUser.as_view(), name='follow_user'),
    path('follow/<int:id>/unfollow/', FollowUser.as_view(), name='unfollow_user'),
    path('search/username/<str:username_query>', UserSearchByUsername.as_view(), name='search'),
    path('search/follow/username/<str:username_query>', UserSearchFollow.as_view(), name='search_follow'),
    path('me/friend/exp/', MyFriendListWithExp.as_view(), name='friend_exp'),
]
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .api_views import MeAPIView, RegisterAPIView, DataLogin, MyLearnProgressAPI


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('data_login/', DataLogin.as_view(), name='data_login'),
    path('me/', MeAPIView.as_view(), name='me'),
    path('me/learn_progress/', MyLearnProgressAPI.as_view(), name='my_learn_progress'),
]
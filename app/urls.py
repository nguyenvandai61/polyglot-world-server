from .auth import urls
from django.urls import path, include

urlpatterns = [
    path('auth/', include("app.auth.urls"), name="auth"),
    path('country/', include("app.api.country.urls"), name="country"),
    path('language/', include("app.api.language.urls"), name="language"),
    path('user/', include("app.api.user.urls"), name="user"),
]
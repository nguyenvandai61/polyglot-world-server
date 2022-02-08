from django.urls import include, re_path
from django.urls import include, path
from django.conf.urls import url

from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app import view_sets
from rest_framework_simplejwt.authentication import JWTAuthentication

router = routers.DefaultRouter()
router.register(r'users', view_sets.UserViewSet)
router.register(r'groups', view_sets.GroupViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="PolyglotWorld Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[
        JWTAuthentication,
    ],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
    path('api/', include('app.urls'), name='api'),
]

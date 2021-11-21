from django.urls import include, path
from rest_framework import routers
from app import view_sets

router = routers.DefaultRouter()
router.register(r'users', view_sets.UserViewSet)
router.register(r'groups', view_sets.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include('app.urls'), name='api'), 
    path('', include(router.urls)),
]
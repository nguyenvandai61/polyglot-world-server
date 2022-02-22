from django.urls import include, path
from .api import NotificationList, MyNotificationList

urlpatterns = [
	path('', NotificationList.as_view(), name='notification-list'),
	path('me/', MyNotificationList.as_view(), name='my-notification-list'),
]

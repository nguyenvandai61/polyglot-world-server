from app.models.Notification import Notification
from rest_framework import generics, permissions

from app.mserializers.NotificationSerializers import NotificationSerializers
from app.utils.paginations import SmallResultsSetPagination


class NotificationList(generics.ListAPIView):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializers
	permission_classes = [permissions.IsAdminUser]
 
 
class MyNotificationList(generics.ListAPIView):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializers
	pagination_class = SmallResultsSetPagination
	permission_classes = [permissions.IsAuthenticated]
	
	def get_queryset(self):
		user = self.request.user
		return Notification.objects.filter(user=user)
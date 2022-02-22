from rest_framework import serializers
from app.models.Notification import Notification

class NotificationSerializers(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = '__all__'
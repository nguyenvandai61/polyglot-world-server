from django.db import models


class Notification(models.Model):
	user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
	message = models.CharField(max_length=200)
	time_stamp = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)

	def __str__(self):
		return self.message

	class Meta:
		ordering = ['-time_stamp']
		db_table = 'notifications'
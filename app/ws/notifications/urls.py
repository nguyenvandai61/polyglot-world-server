
# Notifications URLs
url_patterns = [
	# /notifications/
	(r'/notifications/', NotificationsHandler),
	# /notifications/<notification_id>
	(r'/notifications/(\d+)', NotificationHandler),
]


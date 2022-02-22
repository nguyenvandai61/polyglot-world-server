
class NotificationsServices():
	def __init__(self, db):
		self.db = db

	def get_notifications(self, user_id):
		notifications = self.db.execute(
			'SELECT * FROM notifications WHERE user_id = ?', (user_id, )
		).fetchall()

		return notifications

	def add_notification(self, user_id, message):
		self.db.execute(
			'INSERT INTO notifications (user_id, message) VALUES (?, ?)',
			(user_id, message)
		)
		self.db.commit()

	def delete_notification(self, user_id, notification_id):
		self.db.execute(
			'DELETE FROM notifications WHERE user_id = ? AND id = ?',
			(user_id, notification_id)
		)
		self.db.commit()
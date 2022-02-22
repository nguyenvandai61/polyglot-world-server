from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NotificationConsumer(AsyncJsonWebsocketConsumer):

	async def connect(self):
		"""
		Called when the websocket is handshaking as part of initial connection.
		"""
		try:
			token = self.scope['url_route']['kwargs']['token']
			user = await self.get_user(token)
			if user:
				self.user = user

				# Join group
				await self.channel_layer.group_add(
					self.user.username,
					self.channel_name
				)
    
				await self.accept()
				await self.send_notifications()
			else:
				await self.close()
		except KeyError:
			await self.close()
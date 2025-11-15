import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatRoom, Message
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender_id = data['sender_id']
        message = data['message']

        sender = await self.get_user(sender_id)
        room = await self.get_room(self.room_id)

        msg = Message.objects.create(room=room, sender=sender, text=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender.name,
                "timestamp": str(msg.timestamp),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @staticmethod
    async def get_user(user_id):
        return User.objects.get(id=user_id)

    @staticmethod
    async def get_room(room_id):
        return ChatRoom.objects.get(id=room_id)

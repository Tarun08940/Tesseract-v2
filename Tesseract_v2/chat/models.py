from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from teams.models import Team

class ChatRoom(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="chatrooms")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email}: {self.text[:20]}"

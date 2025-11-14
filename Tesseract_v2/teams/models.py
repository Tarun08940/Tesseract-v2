from django.db import models
from users.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_teams")
    members = models.ManyToManyField(User, related_name="teams")  # team members
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

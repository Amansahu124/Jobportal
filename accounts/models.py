from django.db import models

from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()  # The notification text
    created_at = models.DateTimeField(auto_now_add=True)  # Time when notification was created
    read = models.BooleanField(default=False)  # True if the user has read it

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"





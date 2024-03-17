from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class NotificationToGroup(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

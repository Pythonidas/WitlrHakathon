from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
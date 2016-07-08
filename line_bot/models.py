from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.textField(default="")
    sender = models.textField(default="")
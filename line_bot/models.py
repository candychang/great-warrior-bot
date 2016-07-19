from django.db import models

# Create your models here.

class Request(models.Model):
	itemrequest = models.TextField(default='')
	url = models.TextField(default='')
	size = models.TextField(default='')
	itemcolor = models.TextField(default='')

class Message(models.Model):
    content = models.TextField(default="")
    sender = models.TextField(default="")


from django.db import models

# Create your models here.
class Form(models.Model):
	text = models.TextField(default='')
from django.db import models
from django.forms import ModelForm, TextInput

EMPTY_ITEM_ERROR = "You can't have an empty list item"
# Create your models here.
class UserModel(models.Model):
	username = models.TextField()
	line_id = models.TextField()

class Request(models.Model):
	user = models.ForeignKey(UserModel, default = 1 )
	itemrequest = models.TextField(default='')
	url = models.TextField(default='')
	size = models.TextField(default='')
	itemcolor = models.TextField(default='')
	cost = models.TextField(default='')


class Message(models.Model):
    content = models.TextField(default="")
    sender = models.TextField(default="")

	
class RequestForm(ModelForm):

	class Meta:
		model = Request
		fields = ['itemrequest', 'url', 'size', 'itemcolor', 'cost',]
		widgets = {
			'itemrequest' : TextInput(attrs={
				'placeholder': 'Item',
				'class': 'form-control input-lg',
			}),
			'url' : TextInput(attrs={
				'placeholder': 'URL',
				'class': 'form-control input-lg',
			}),
			'size' : TextInput(attrs={
				'placeholder': 'Size', 
				'class': 'form-control input-lg',
			}),
			'itemcolor' : TextInput(attrs={
				'placeholder': 'Color',
				'class': 'form-control input-lg',
			}),
			'cost' : TextInput(attrs={
				'placeholder': 'Cost',
				'class': 'form-control input-lg',
			}),

		}

		error_messages = {
			'itemrequest': {'required': EMPTY_ITEM_ERROR},
			'url': {'required': EMPTY_ITEM_ERROR}
		}


class Status(models.Model):
	ordered = models.TextField(default='')
	issue = models.TextField(default='')
	newOrder = models.TextField(default='')


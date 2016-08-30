from django.db import models
from django.forms import ModelForm, TextInput, Textarea, Select

EMPTY_ITEM_ERROR = "You can't submit an order without specifying your item"
EMPTY_URL_ERROR = "You can't submit an order without a link to the item"
# Create your models here.
class User(models.Model):
	username = models.TextField()
	line_id = models.TextField()

class Request(models.Model):
	user = models.ForeignKey(User, default = 1 )
	item = models.TextField(default='')
	url = models.TextField(default='')
	details = models.TextField(default='')
	quantity = models.IntegerField(choices= [(x, x) for x in range(1, 11)])
	cost_limit = models.TextField(default='')


class Message(models.Model):
    content = models.TextField(default="")
    sender = models.TextField(default="")

class RequestForm(ModelForm):

	class Meta:
		model = Request
		fields = ['item', 'url', 'details', 'quantity', 'cost_limit',]
		widgets = {
			'item' : TextInput(attrs={
				'placeholder': 'Item',
				'class': 'form-control',
			}),
			'url' : TextInput(attrs={
				'placeholder': 'URL',
				'class': 'form-control',
			}),
			'details' : Textarea(attrs={
				'placeholder': 'Input details like color or size here', 
				'class': 'form-control',
			}),
			'quantity' : Select(attrs={
				'class': 'form-control',
			}),
			'cost_limit' : TextInput(attrs={
				'placeholder': 'Desired cost limit',
				'class': 'form-control',
			}),

		}

		error_messages = {
			'item': {'required': EMPTY_ITEM_ERROR},
			'url': {'required': EMPTY_URL_ERROR}
		}


class Status(models.Model):
	ordered = models.TextField(default='')
	issue = models.TextField(default='')
	newOrder = models.TextField(default='')


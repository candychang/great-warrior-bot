from django import forms

from line_bot.models import Request

EMPTY_ITEM_ERROR = "You can't have an empty list item"
class RequestForm(forms.models.ModelForm):

	class Meta:
		model = Request
		fields = ('itemrequest',)
		widgets = {
			'itemrequest' : forms.fields.TextInput(attrs={
				'placeholder': 'Item',
				'class': 'form-control input-lg',
			}),
		}

		error_messages = {
			'itemrequest': {'required': "You can't have an empty list item"}
		}
from django import forms

from line_bot.models import Request

EMPTY_ITEM_ERROR = "You can't have an empty list item"
class RequestForm(forms.models.ModelForm):

	class Meta:
		model = Request
		fields = ('itemrequest', 'url', 'size', 'itemcolor',)
		widgets = {
			'itemrequest' : forms.fields.TextInput(attrs={
				'placeholder': 'Item',
				'class': 'form-control input-lg',
			}),
			'url' : forms.fields.TextInput(attrs={
				'placeholder': 'URL',
				'class': 'form-control input-lg',
			}),
			'size' : forms.fields.TextInput(attrs={
				'placeholder': 'Size',
				'class': 'form-control input-lg',
			}),
			'itemcolor' : forms.fields.TextInput(attrs={
				'placeholder': 'Color',
				'class': 'form-control input-lg',
			}),
		}

		error_messages = {
			'itemrequest': {'required': EMPTY_ITEM_ERROR},
			'url': {'required': EMPTY_ITEM_ERROR}
		}
from django import forms

class RequestForm(forms.Form):
	itemrequest = forms.CharField(
		widget=forms.fields.TextInput(attrs={
			'placeholder': 'Item',
			'class': 'form-control input-lg',}),
		)
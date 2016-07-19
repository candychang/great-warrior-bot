from django.shortcuts import redirect, render
from django.http import HttpResponse
from line_bot.models import Request
from line_bot.forms import RequestForm

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	
def form_page(request):		
	return render(request, 'form.html', {'form': RequestForm()})

def confirm_page(request):
	 return render(request, 'confirm.html')

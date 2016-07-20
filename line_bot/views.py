from django.shortcuts import redirect, render
from django.http import HttpResponse
from line_bot.models import Request, RequestForm


# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	
def form_page(request):	
	form = RequestForm()
	return render(request, 'form.html', {'form': form})

def confirm_page(request):
	 return render(request, 'confirm.html')

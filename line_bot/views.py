from django.shortcuts import render
from django.http import HttpResponse
from line_bot.models import Request

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	
def form_page(request):
	if request.method == 'POST':
		new_item = request.POST
		Request.objects.create(**new_item)
	else:
		new_item = {}
		
	return render(request, 'form.html', new_item,)


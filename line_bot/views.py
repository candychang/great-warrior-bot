from django.shortcuts import redirect, render
from django.http import HttpResponse
from line_bot.models import Request

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	
def form_page(request):
	if request.method == 'POST':
		new_item = request.POST.copy()
		del new_item['csrfmiddlewaretoken']
		Request.objects.create(**new_item)
		return redirect('request-confirm')
	else:
		new_item = {}
		
	return render(request, 'form.html', new_item,)

def confirm_page(request):
	 return render(request, 'confirm.html')

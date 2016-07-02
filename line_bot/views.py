from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	
def form_page(request):
	if request.method == 'POST':
		return HttpResponse(request.POST.values())
	return render(request, 'form.html')
	
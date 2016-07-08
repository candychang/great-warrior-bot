from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api
from django.conf import settings

# Create your views here.
def home_page(request):
	return HttpResponse('<html><p>Welcome</p></html>')

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        
        signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']

        if line_api.validate_signature(request.body, signature, settings.LINE_SECRET):
            return HttpResponse('<html><p>RECEIVED</p></html>')
        else:
            return HttpResponseBadRequest()


    elif request.method == 'GET':
        return HttpResponse('<html><p>GET</p></html>')

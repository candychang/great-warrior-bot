from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api

# Create your views here.
def home_page(request):
	return HttpResponse('<html><p>Welcome</p></html>')

@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']
    return HttpResponse('<html><p>RECEIVED</p></html>')
    # if line_api.validate_signature(request.body, signature, LINE_SECRET):
    #     return HttpResponse('<html><p>RECEIVED</p></html>')
    # else:
    #     return HttpResponseBadRequest()
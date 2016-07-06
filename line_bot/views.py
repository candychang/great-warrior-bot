from django.shortcuts import render
from django.http import HttpResponse
from line_bot import line_api

# Create your views here.
def home_page(request):
	return HttpResponse('<html><p>Welcome</p></html>')

@csrf_exempt
def callback(request):
    return HttpResponse('<html><p>RECEIVED</p></html>')
    # signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']
    # if line_api.validate_signature(request.body, signature, LINE_SECRET):
    #     return HttpResponse('<html><p>RECEIVED</p></html>')
    # else:
    #     return HttpResponseBadRequest()
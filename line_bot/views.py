from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api
from django.conf import settings
import json
from line_bot.models import Message


# Create your views here.
def home_page(request):
	return HttpResponse('<html><p>Welcome</p></html>')

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        
        signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']
        received_json_data = json.loads(request.body.decode("utf-8"))
        for r in received_json_data[result]:
            c = r.content
            m = Message(sender="test", content=c.text)
            m.save()

        return HttpResponse()

        # if line_api.validate_signature(request.body, signature, settings.LINE_SECRET):
        #     return render(request, 'callback.html', {'sig': signature})
        # else:
        #     return HttpResponseBadRequest()


    elif request.method == 'GET':
        m = Message.objects.count()
        return render(request, 'callback.html', {'sig': m.count()})

from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api
from django.conf import settings
import json
import requests
from line_bot.models import Message, Request

# Create your views here.
def home_page(request):
	return render(request, 'home.html')

@csrf_exempt
def callback(request):

    if request.method == 'POST':

        signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']
        if line_api.validate_signature(request.body, signature, settings.LINE_SECRET):
            received_json_data = json.loads(request.body.decode("utf-8"))
            sending_user = ""
            sent_text = ""
            for event in received_json_data["result"]:
                c = r["content"]
                sending_user = sending_user + c["from"]
                sent_text= sent_text + c["text"]
                m = Message(sender=sending_user, content=sent_text)
                m.save()
            messages = Message.objects.all()
            index = len(messages)
            last_message = messages[index - 1]
            to_send = "HI! This is LineBot. You sent me this message: " + last_message.content
            sending_user = last_message.sender
            r = line_api.send_message(to_send, sending_user)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()
        


    elif request.method == 'GET':
        m = Message.objects.all()
        index = len(m)
        if index > 0:
            return render(request, 'callback.html', {'messages': m})
        else:
            return render(request, 'callback.html', {'sig': "get"})

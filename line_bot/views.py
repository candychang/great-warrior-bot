from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api
from django.conf import settings
import json
import requests
from line_bot.models import Message


# Create your views here.
def home_page(request):
	return HttpResponse('<html><p>Welcome</p></html>')

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        
        signature = request.META['HTTP_X_LINE_CHANNELSIGNATURE']
        received_json_data = json.loads(request.body.decode("utf-8"))
        sending_user = ""
        sent_text = ""
        for r in received_json_data["result"]:
            c = r["content"]
            sending_user = sending_user + c["from"]
            sent_text= sent_text + c["text"]
            m = Message(sender=sending_user, content=sent_text)
            m.save()

        return HttpResponse()

        # if line_api.validate_signature(request.body, signature, settings.LINE_SECRET):
        #     return render(request, 'callback.html', {'sig': signature})
        # else:
        #     return HttpResponseBadRequest()


    elif request.method == 'GET':
        messages = Message.objects.all()
        index = len(messages)
        if index > 0:
            last_message = messages[index - 1]
            to_send = "HI! This is LineBot. You sent me this message: " + last_message.content
            sending_user = last_message.sender
            headers = {'Content-type': "application/json",
                    'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
                    'X-Line-ChannelSecret': settings.LINE_SECRET,
                    'X-Line-Trusted-User-With-ACL': settings.LINE_MID }
            r = line_api.send_message(to_send, sending_user, headers)
            return render(request, 'callback.html', {'sig': r.text})
        else:
            return render(request, 'callback.html', {'sig': "get"})


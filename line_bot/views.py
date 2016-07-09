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
            sending_user = c["from"]
            sent_text= c["text"]
            m = Message(sender=sending_user, content=sent_text)
            m.save()

        to_send = "HI! This is LineBot. You sent me this message: " + sent_text
        headers = {'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
                   'X-Line-ChannelSecret': settings.LINE_SECRET,
                   'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

        return line_api.send_message(to_send, sending_user, headers)

        # if line_api.validate_signature(request.body, signature, settings.LINE_SECRET):
        #     return render(request, 'callback.html', {'sig': signature})
        # else:
        #     return HttpResponseBadRequest()


    elif request.method == 'GET':
        m = Message.objects.all()
        if m:
            text= ""
            for message in m:
                text = text + message.content + "\n"
            return render(request, 'callback.html', {'sig': text})
        else:
            return render(request, 'callback.html', {'sig': "get"})


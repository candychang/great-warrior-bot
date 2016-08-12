from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from line_bot import line_api
from django.conf import settings
import json
import requests
from line_bot.models import *

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
            for r in received_json_data["result"]:
                c = r["content"]
                sending_user = sending_user + c["from"]
                sent_text= sent_text + c["text"]
                m = Message(sender=sending_user, content=sent_text)
                m.save()
                if m.content == "test":
                    to_send = "HI! This is LineBot. The test succeeded!"
                    sending_user = m.sender
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

def form_page(request):	
	form = RequestForm()
	return render(request, 'form.html', {'form': form})
def confirm_page(request):
	if request.method == 'POST':
		form = RequestForm(request.POST)
		if form.is_valid():
			new_form = form.save()
			return render(request, 'confirm.html', {'order' : new_form})
def orders_page(request, user_id):
	if request.method == 'GET':
		user = UserModel.objects.get(id=user_id)
		order = user.request_set.all()
	return render(request, 'orders.html', {'order' : order} )


def admin_orders_page(request):
	if request.method == 'GET':
		user = UserModel.objects.all()
	return render(request, 'adminorders.html', {'user' : user} ) 

def simulate_bot(request):
    if request.method == 'POST':
        form = request.POST
        mid = str(form.get("recipient"))
        message = str(form.get("message"))
        sent = line_api.send_message(message, mid)
        if sent:
            return render(request, 'simulate.html', {'status': sent.status_code, 'm': None})
        else:
            return render(request, 'simulate.html', {'status': sent.status_code, 'm': None})
    else:
        m = Message.objects.last()
        return render(request, 'simulate.html', {'status': "Last received message", 'm': m})


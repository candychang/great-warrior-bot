import hashlib
import hmac
import base64
import json
import requests
from django.http import HttpResponse
from django.conf import settings


HEADERS =  {'Content-Type': "application/json",
            'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
            'X-Line-ChannelSecret': settings.LINE_SECRET,
            'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

"""
Validate LINE signature on HTTP requests

Args:
request_body: Body of HTTP request
signature: Request header 'X-LINE-ChannelSignature'
secret: Secret used to create digest from request_body

Returns:
bool: True if valid, false otherwise
"""


def validate_signature(request_body, signature, secret):
    if (request_body and signature and secret):
        secret = secret.encode("utf-8")
        sig = signature.encode("utf-8")

        generated_sig = base64.b64encode(hmac.new(secret, request_body, digestmod=hashlib.sha256).digest())
        
        return hmac.compare_digest(generated_sig, sig)

    else:
        return False


"""
Send message in reply to user

Args:
message_body: Text to send to user
recipient: User who will receive the message
headers: Http headers

Returns:
r: the response object
"""

def send_message(message_body, recipient, url = 'https://trialbot-api.line.me/v1/events'):
    data = {"to": [recipient], 
            "toChannel": 1383378250,
            "eventType": "138311608800106203",
            "content":{"contentType":1,"toType":1, "text": message_body}}
    r = requests.post(url, data=json.dumps(data), headers=HEADERS)
    return r

"""
Parse LINE event and send appropriate reply

Args:
event: JSON data for one LINE event

Returns:
r: the response object
"""

def parse_and_reply(event):
    pass
    


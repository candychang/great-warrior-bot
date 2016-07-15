import hashlib
import hmac
import base64
import json
import requests
from django.http import HttpResponse

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

        secret = bytes(secret)

        generated_sig = base64.b64encode(hmac.new(secret, request_body, digestmod=hashlib.sha256).digest())

        return signature == generated_sig

    else:
        return False


def send_message(message_body, recipient, headers):

    url = 'https://trialbot-api.line.me/v1/events'
    data = {"to": [recipient], 
            "toChannel": 1383378250,
            "eventType": "138311608800106203",
            "content":{"contentType":1,"toType":1, "text": message_body}}

    headers = headers
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r
    


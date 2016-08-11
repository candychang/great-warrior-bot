# import hashlib
# import hmac
# import base64
# import json
# import requests
# from django.http import HttpResponse
# from django.conf import settings
# from line_bot import constants


# HEADERS =  {'Content-Type': "application/json",
#             'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
#             'X-Line-ChannelSecret': settings.LINE_SECRET,
#             'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

# """
# Validate LINE signature on HTTP requests

# Args:
# request_body: Body of HTTP request
# signature: Request header 'X-LINE-ChannelSignature'
# secret: Secret used to create digest from request_body

# Returns:
# bool: True if valid, false otherwise
# """


# def validate_signature(request_body, signature, secret):
#     if (request_body and signature and secret):
#         secret = secret.encode("utf-8")
#         sig = signature.encode("utf-8")

#         generated_sig = base64.b64encode(hmac.new(secret, request_body, digestmod=hashlib.sha256).digest())
        
#         return hmac.compare_digest(generated_sig, sig)

#     else:
#         return False


# """
# Send message in reply to user

# Args:
# message_body: Text to send to user
# recipient: User who will receive the message
# headers: Http headers

# Returns:
# r: the response object
# """

# def send_message(message_body, recipient):
#     data = {"to": [recipient], 
#             "toChannel": 1383378250,
#             "eventType": "138311608800106203",
#             "content":{"contentType":1,"toType":1, "text": message_body}}
#     url = 'https://trialbot-api.line.me/v1/events'
#     r = requests.post(url, data=json.dumps(data), headers=HEADERS)
#     return r

# """
# Parse LINE event and returns relevant info

# Args:
# event: Dictionary of data for one LINE event

# Returns:
# Event object - either messageEvent or operationEvent,
#                depending on the event type

# """

# def parse_event(event):
#     if event["eventType"] == constants.MESSAGE_EVENT:
#         return MessageEvent(event["content"])
#     elif event["eventType"] == constants.OPERATION_EVENT:
#         return OperationEvent(event["content"])



# def fetch_media(message_id):
#     pass


# class MessageEvent(object):
#     def __init__(self, content_data):
#         self.message_id = content_data["id"]
#         self.sender = content_data["from"]
#         self.content_type = content_data["contentType"]
#         self.content = self.get_content(content_data)

#     def get_content(self, content_data):
#         content_type = content_data['contentType']
#         if content_type == constants.TEXT:
#             return TextContent(content_data['text'])
#         elif content_type == constants.IMAGE:
#             return fetch_media(self.message_id)
#         elif content_type == constants.STICKER:
#             return StickerContent(content_data['contentMetadata'])
#         else:
#             return None

# class TextContent(object):
#     def __init__(self, content_text):
#         text = content_text

# class ImageContent(object):
#     def __init__(self, content_metadata):
#         pass

# class StickerContent(object):
#     def __init__(self, content_metadata):
#         pass


# class OperationEvent(object):
#     def __init__(self, content_data):
#         pass

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

def send_message(message_body, recipient, headers):

    url = 'https://trialbot-api.line.me/v1/events'
    data = {"to": [recipient], 
            "toChannel": 1383378250,
            "eventType": "138311608800106203",
            "content":{"contentType":1,"toType":1, "text": message_body}}

    headers = headers
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r
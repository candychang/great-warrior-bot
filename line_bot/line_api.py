import hashlib
import hmac
import base64
import json
import requests
from django.http import HttpResponse
from django.conf import settings
from line_bot import constants
from PIL import Image
from io import StringIO


def validate_signature(request_body, signature, secret):
    """
    Validate LINE signature on HTTP requests

    Args:
    request_body: Body of HTTP request
    signature: Request header 'X-LINE-ChannelSignature'
    secret: Secret used to create digest from request_body

    Returns:
    True if valid, False otherwise
    """
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

def send_message(message_body, recipient):

    url = 'https://trialbot-api.line.me/v1/events'

    data = {"to": [recipient], 
            "toChannel": 1383378250,
            "eventType": "138311608800106203",
            "content":{"contentType":1,"toType":1, "text": message_body}}

    headers = {'Content-Type': "application/json",
                'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
                'X-Line-ChannelSecret': settings.LINE_SECRET,
                'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r




def parse_event(event):
    """
    Parse a LINE event and return relevant Event object

    Args:
    event: Dictionary of data for one LINE event

    Returns:
    Event object: either MessageEvent or OperationEvent,
                   depending on the event type

    """
    if event["eventType"] == constants.MESSAGE_EVENT:
        return MessageEvent(event["content"])
    elif event["eventType"] == constants.OPERATION_EVENT:
        return OperationEvent(event["content"])

def fetch_image(message_id):
    """
    Fetches the binary image data from message, converts it to image

    Args:
    message_id: The LINE ID of the message

    Returns:
    content: the image
    """
    content = None
    url = "https://trialbot-api.line.me/v1/bot/message/" + str(message_id) + "/content"
    headers = {'Content-Type': "application/json",
                'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
                'X-Line-ChannelSecret': settings.LINE_SECRET,
                'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        content = Image.open(StringIO(r.content))

    return content

def fetch_profile(mid):
    """
    Fetches the profile for a LINE user

    Args:
    mid: The LINE member ID of a user

    Returns:
    content: A dictionary with profile information, following LINE API data model
             {"statusMessage": "<Status Message>",
              "pictureUrl": "<URL for image>",
              "mid": "<User ID>",
              "displayName": "<Display Name>" }
    """
    profile = None
    url = "https://trialbot-api.line.me/v1/profiles?mids=" + str(mid)
    headers = {'Content-Type': "application/json",
                'X-Line-ChannelID': settings.LINE_CHANNEL_ID,
                'X-Line-ChannelSecret': settings.LINE_SECRET,
                'X-Line-Trusted-User-With-ACL': settings.LINE_MID }

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        content = r.json()
        profile = content["contacts"][0]

    return profile



class MessageEvent(object):
    """
    Class representing a LINE message object. Takes in a LINE message's
    content data as a dictionary, and saves relevant info as attributes

    Attributes:
    message_id: ID of the message. Used for LINE API requests
    sender: LINE member ID of the message sender. Use this to specify who to reply to
    content_type: Type of message (text, image, sticker supported as of now)
    content: a Content object containing relevant information
    """

    def __init__(self, content_data):
        self.message_id = content_data["id"]
        self.sender = content_data["from"]
        self.content_type = content_data["contentType"]
        self.content = self.retrieve_content(content_data)

    def retrieve_content(self, content_data):
        """
        Creates Content object based on a message event's content type

        Args: 
        content_data: dictionary of content data

        Returns:
        Content object or None: Currently handles text, image and sticker types.
        If the message contains unsupported content type, returns None
        """
        content_type = content_data["contentType"]
        if content_type == constants.TEXT:
            return content_data["text"]
        elif content_type == constants.IMAGE:
            return fetch_image(self.message_id)
        elif content_type == constants.STICKER:
            return content_data["contentMetadata"]
        else:
            return None

class TextContent(object):
    def __init__(self, content_text):
        pass


class ImageContent(object):
    def __init__(self, content_metadata):
        pass

class StickerContent(object):
    def __init__(self, content_metadata):
        pass


class OperationEvent(object):
    """
    Class representing a LINE operation object. Takes in a LINE operation's
    content data as a dictionary, and saves relevant info as attributes

    Attributes:
    message_id: ID of the message. Used for LINE API requests
    op_type: Type of message (text, image, sticker supported as of now)
    mid: the LINE member ID of acting user
    """
    def __init__(self, content_data):
        self.revision = content_data["revision"]
        self.op_type = content_data["opType"]
        self.mid = content_data["params"][0]
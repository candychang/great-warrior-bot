import hashlib
import hmac
import base64

"""
Validate LINE signature on HTTP requests

Args:
request_body: Body of HTTP request
signature: Request header 'X-LINE-ChannelSignature'
secret: Secret used to create digest from request_body

Returns:
bool: True if valid, false otherwise
"""

# Get an instance of a logger
logger = logging.getLogger(__name__)


def validate_signature(request_body, signature, secret):
    if (request_body and signature and secret):

        request_body = bytes(request_body)
        secret = bytes(secret)

        generated_sig = base64.b64encode(hmac.new(secret, request_body, digestmod=hashlib.sha256).digest())

        return hmac.compare_digest(signature, generated_sig)

    else:
        return False

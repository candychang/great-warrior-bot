import hashlib
import hmac
import base64

"""
Validate LINE signature on HTTP requests

Args:
request_body (bytes): Body of HTTP request
signature (string): Request header 'X-LINE-ChannelSignature'
secret (string): Secret used to create digest from request_body

Returns:
bool: True if valid, false otherwise
"""

def validate_signature(request_body, signature, secret):
    if (request_body and signature and secret):

        message = bytes(request_body).encode('utf-8')
        secret = bytes(secret).encode('utf-8')

        generated_sig = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())

        return hmac.compare_digest(signature, generated_sig)

    else:
        return false

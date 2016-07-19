from django.test import TestCase, RequestFactory
from line_bot.views import *
from line_bot.models import Request
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from line_bot.line_api import *

# Create your tests here.
class homeTest(TestCase):
	def test_home_url(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
	def test_home_correctect(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class apiTest(TestCase):
	def setUp(self):
	 	self.factory = RequestFactory()


	def test_validation_fn(self):
		channel_sig ='i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgs='
		message = "message".encode('utf-8')
		secret = "secret"
		result = line_api.validate_signature(message, channel_sig, secret)
		self.assertTrue(result)


	def test_validation(self):
		request_data = json.dumps({"result":[
									  {
									    "from":"u2ddf2eb3c959e561f6c9fa2ea732e7eb8",
									    "fromChannel":1341301815,
									    "to":["u0cc15697597f61dd8b01cea8b027050e"],
									    "toChannel":1441301333,
									    "eventType":"138311609000106303",
									    "id":"ABCDEF-12345678901",
									    "content": {
									      "id":"325708",
									      "contentType":1,
									      "from":"uff2aec188e58752ee1fb0f9507c6529a",
									      "createdTime":1332394961610,
									      "to":["u0a556cffd4da0dd89c94fb36e36e1cdc"],
									      "toType":1,
									      "text":"Hello, BOT API Server!"
									    }
									  }
									]})
		request = self.factory.post('/callback', data=request_data, content_type='application/json', follow=False, secure=True)
		request.META['HTTP_X_LINE_CHANNELSIGNATURE'] = '/xZcekiWAiCrwq5dC+wBwBf6gQ33i1jRAo01KAVO3/U='
		response = callback(request)
		self.assertEqual(response.status_code, 400)

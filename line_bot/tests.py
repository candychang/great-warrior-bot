from django.test import TestCase, RequestFactory
from line_bot.views import *
from line_bot.models import Request
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from line_bot.line_api import *

class apiTest(TestCase):

	def test_valid_sig(self):
		channel_sig ='i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgs='
		message = "message".encode('utf-8')
		secret = "secret"
		result = line_api.validate_signature(message, channel_sig, secret)
		self.assertTrue(result)


	def test_invalid_sig(self):
		channel_sig ='i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgsb'
		message = "message".encode('utf-8')
		secret = "secret"
		result = line_api.validate_signature(message, channel_sig, secret)
		self.assertFalse(result)

	# TODO
	def test_send_message(self):
		line_api.send_message("test", "12345678", url="https://bot-staging.herokuapp.com/")

		pass

	# TODO
	def test_parse_text(self):
		event = {
				  "id": "ABCDEF-12345678901",
				  "eventType": "138311609000106303",
				  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
				  "fromChannel": 1341301815,
				  "to": [
				    "u0a556cffd4da0dd89c94fb36e36e1cdc"
				  ],
				  "toChannel": 1441301333,
				  "content": {
				    "id": "325708",
				    "contentType": 1,
				    "from": "uff2aec188e58752ee1fb0f9507c6529a",
				    "createdTime": 1462629479859,
				    "to": [
				      "u0a556cffd4da0dd89c94fb36e36e1cdc"
				    ],
				    "toType": 1,
				    "contentMetadata": {
				    },
				    "text": "test",
				    "location": None
				  }
				}

	#TODO
	def test_parse_sticker(self):
		event =   {
				  "id": "ABCDEF-12345678901",
				  "eventType": "138311609000106303",
				  "from": "u206d25c2ea6bd87c17655609a1c37cb8",
				  "fromChannel": 1341301815,
				  "to": [
				    "u0a556cffd4da0dd89c94fb36e36e1cdc"
				  ],
				  "toChannel": 1441301333,
				  "content": {
				    "id": "325708",
				    "contentType": 8,
				    "from": "uff2aec188e58752ee1fb0f9507c6529a",
				    "createdTime": 1462629479859,
				    "to": [
				      "u0a556cffd4da0dd89c94fb36e36e1cdc"
				    ],
				    "toType": 1,
				    "contentMetadata": {
				      "STKPKGID": "1",
				      "STKID": "1",
				      "STKVER": "100",
				      "STKTXT": "[zzz]"
				    },
				    "text": None,
				    "location": None
				  }
				}
	#TODO
	def test_parse_add_friend(self):
		pass

	#TODO
	def test_add_user_info(self):
		pass

		
class callbackTest(TestCase):
	def setUp(self):
	 	self.factory = RequestFactory()

	def test_invalid_message(self):
		headers = {'HTTP_X_LINE_CHANNELSIGNATURE': 'i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgs='}
		r = requests.post(url, data=json.dumps(data), headers=HEADERS)
		pass

# Create your tests here.
EMPTY_ITEM_ERROR = "You can't have an empty list item"
class RequestFormTest(TestCase):

	# def test_form_input_placeholder_css(self):
		# form = RequestForm()
		# self.assertIn('placeholder="Item"', form.as_p())
		# self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation(self):
		form = RequestForm(data={'itemrequest': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['itemrequest'], [EMPTY_ITEM_ERROR])

	def test_form_page_renders_home_template(self):
		response = self.client.get('/request/new')
		self.assertTemplateUsed(response, 'form.html')
		
	def test_from_page_uses_item_form(self):
		response = self.client.get('/request/new')
		self.assertIsInstance(response.context['form'], RequestForm)
		
	def test_from_is_saved(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST = {"itemrequest": 'A new item',
						"url":  'A new url',
						"size": 'Item size',
						"itemcolor": 'Item color'}

		response = confirm_page(request)
		content = response.content.decode()
		
		self.assertEqual(Request.objects.count(), 1)
		new_item = Request.objects.first()
		self.assertEqual(new_item.itemrequest, 'A new item')
		self.assertEqual(new_item.url, 'A new url')
		self.assertEqual(new_item.size, 'Item size')
		self.assertEqual(new_item.itemcolor, 'Item color')

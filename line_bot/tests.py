from django.test import TestCase, SimpleTestCase, Client
from line_bot.views import *
from line_bot.models import Request
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from line_bot.line_api import *
from line_bot import constants
from unittest.mock import Mock, patch, call
from unittest import skipIf


EMPTY_ITEM_ERROR = "You can't have an empty list item"
class RequestFormTest(TestCase):

	def test_form_input_placeholder_css(self):
		form = RequestForm()
		self.assertIn('placeholder="Item"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

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


class ValidateSigTest(TestCase):

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


#TODO
class ParseEventTest(SimpleTestCase):
	
	def test_parse_text(self):
		event = constants.TEXT_EVENT
		result = line_api.parse_event(event)
		self.assertIsInstance(result, MessageEvent)
		self.assertEqual(result.content_type, constants.TEXT)
		self.assertEqual(result.content, constants.SAMPLE_MESSAGE_TEXT)


	def test_parse_sticker(self):
		event = constants.STICKER_EVENT
		result = line_api.parse_event(event)
		self.assertIsInstance(result, MessageEvent)
		self.assertEqual(result.content_type, constants.STICKER)
		self.assertEqual(result.content, constants.SAMPLE_STICKER_DATA)

	@patch('line_bot.line_api.fetch_image')
	def test_parse_image(self, mock_fetch):
		mock_image = Mock()
		mock_fetch.return_value = mock_image
		event = constants.IMAGE_EVENT
		result = line_api.parse_event(event)
		self.assertIsInstance(result, MessageEvent)
		self.assertEqual(result.content_type, constants.IMAGE)
		self.assertEqual(result.content, mock_image)


	def test_parse_add_friend(self):
		event = constants.ADD_FRIEND_OPERATION
		result = line_api.parse_event(event)
		self.assertIsInstance(result, OperationEvent)
		self.assertEqual(result.op_type, constants.ADD_FRIEND)
		self.assertEqual(result.mid, SAMPLE_MID)


	def test_block_user(self):
		event = constants.BLOCK_OPERATION
		result = line_api.parse_event(event)
		self.assertIsInstance(result, OperationEvent)
		self.assertEqual(result.type, constants.BLOCK)
		self.assertEqual(result.mid, SAMPLE_MID)

	
#TODO
class BotCommandsTest(TestCase):

	def test_hello(self):
		pass

	def test_bye(self):
		pass

	def test_order(self):
		pass

	def test_help(self):
		pass

	def test_status(self):
		pass

	def test_edit(self):
		pass

	def test_list(self):
		pass
#TODO
class BotFormTest(TestCase):

	
	def test_form_link(self):
		pass

	def test_form_img_query(self):
		pass

	def test_img_saved(self):
		pass

	def test_no_img_to_save(self):
		pass

	def test_correct_confirmation(self):
		pass

@skipIf(constants.SKIP_REAL, "Skipping tests that hit real API server")	
class apiTest(TestCase):
	@patch('line_bot.line_api.validate_signature')
	def test_valid_message(self, mock_sig):
		mock_sig.return_value = True
		DATA = {"result":[
				{
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
				    "from": "uf7d924cd126613f0ad15e13c52deb340",
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
				]
			}
		url = "/callback"
		c = Client()
		r = c.post(url, data=json.dumps(DATA), content_type="application/json", HTTP_X_LINE_CHANNELSIGNATURE='i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgs=')
		self.assertEqual(r.status_code, 200)

	def test_send_message(self):
		response = line_api.send_message("testing", "uf7d924cd126613f0ad15e13c52deb340")
		self.assertEqual(response.status_code, 200)

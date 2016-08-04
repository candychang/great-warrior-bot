from django.test import TestCase, RequestFactory
from line_bot.views import *
from line_bot.models import Request
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from line_bot.line_api import *
from line_bot.constants import *
from unittest.mock import Mock, patch, call, call_args


class validateSigTest(TestCase):

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
@patch('line_bot.line_api.send_message')
class parseTest(TestCase):
	

	def test_parse_text(self, mock_class):
		event = json.dumps(constants.MESSAGE_EVENT)


	def test_parse_sticker(self):
		event = json.dumps(constants.STICKER_EVENT)


	def test_parse_add_friend(self):
		event = json.dumps(constants.ADD_FRIEND_OPERATION)


	def test_block_user(self):
		event = json.dumps(constants.BLOCK_OPERATION)

	def test_add_user_info(self):
		event = json.dupms(constants.CONTACT_INFO)

#TODO
class botCommandsTest(TestCase):

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
class botFormTest(TestCase):

	
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

		
# class apiTest(TestCase):
	# def setUp(self):
	#  	self.factory = RequestFactory()

	# @patch('line_bot.line_api.validate_signature')
	# @patch('line_bot.send_message')
	# def test_valid_message(self, mock_sig, mock_send_message):
	# 	mock_sig.return_value = True
	# 	headers = {'HTTP_X_LINE_CHANNELSIGNATURE': 'i19IcCmVwVmMVz2x4hhmqbgl1KeU0WnXBgoDYFeWNgs='}
	# 	r = requests.post(url, data=json.dumps(DATA), headers=HEADERS)
	# 	self.assertEqual(response.status_code, 200)

	# def test_send_message(self):
	# 	line_api.send_message("test", "12345678", url="https://bot-staging.herokuapp.com/")
	# 	pass


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

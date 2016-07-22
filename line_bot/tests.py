from django.test import TestCase
from line_bot.views import *
from line_bot.models import Request
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
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

class AdminOrderTest(TestCase):
	def test_template
		response = self.client.get('/admin/orders')
		self.assertTemplateUsed(response, 'adminorders.html')











# class homeTest(TestCase):
	# def test_home_url(self):
		# found = resolve('/')
		# self.assertEqual(found.func, home_page)
		
	# def test_home_correctect(self):
		# request = HttpRequest()
		# response = home_page(request)
		# expected_html = render_to_string('home.html')
		# self.assertEqual(response.content.decode(), expected_html)

# class formTest(TestCase):
	# def test_form_url(self):
		# found = resolve('/request/new')
		# self.assertEqual(found.func, form_page)
		
	# def test_form_correct(self):
		# request = HttpRequest()
		# response = form_page(request)
		# expected_html = render_to_string('form.html')
		# self.assertEqual(response.content.decode(), expected_html)
	
	# def test_form_POST_request(self):
		# request = HttpRequest()
		# request.method = 'POST'
		# request.POST = {"itemrequest": 'A new item',
						# "url":  'A new url',
						# "size": 'Item size',
						# "itemcolor": 'Item color'}

		# response = form_page(request)
		# content = response.content.decode()
		# print(repr(request.POST))
		
		# self.assertEqual(Request.objects.count(), 1)
		# new_item = Request.objects.first()
		# self.assertEqual(new_item.itemrequest, 'A new item')
		# self.assertEqual(new_item.url, 'A new url')
		# self.assertEqual(new_item.size, 'Item size')
		# self.assertEqual(new_item.itemcolor, 'Item color')
		
		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/request/confirm')
		
	# def test_form_saving_items(self):
		# request = HttpRequest()
		# form_page(request)
		# self.assertEqual(Request.objects.count(), 0)
		
# class FormModelTest(TestCase):
	# def test_saving_and_retrieving_items(self):
		# first_item = Request()
		# first_item.itemrequest = 'First item'
		# first_item.url = 'First url'
		# first_item.size = 'First size'
		# first_item.itemcolor = 'First color'
		# first_item.save()
		
		# second_item = Request()
		# second_item.itemrequest = 'Second item'
		# second_item.url = 'Second url'
		# second_item.size = 'Second size'
		# second_item.itemcolor = 'Second color'
		# second_item.save()
		
		
		# saved_items = Request.objects.all()
		# self.assertEqual(saved_items.count(), 2)
		
		# first_saved_item = saved_items[0]
		# second_saved_item = saved_items[1]
		
		# self.assertEqual(first_saved_item.itemrequest,'First item')
		# self.assertEqual(first_saved_item.url,'First url')
		# self.assertEqual(first_saved_item.size,'First size')
		# self.assertEqual(first_saved_item.itemcolor,'First color')
		
		# self.assertEqual(second_saved_item.itemrequest,'Second item')
		# self.assertEqual(second_saved_item.url,'Second url')
		# self.assertEqual(second_saved_item.size,'Second size')
		# self.assertEqual(second_saved_item.itemcolor,'Second color')
		
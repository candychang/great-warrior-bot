from django.test import TestCase
from line_bot.views import *
from line_bot.models import Form
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
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

class formTest(TestCase):
	def test_form_url(self):
		found = resolve('/request/new')
		self.assertEqual(found.func, form_page)
		
	def test_form_correct(self):
		request = HttpRequest()
		response = form_page(request)
		expected_html = render_to_string('form.html')
		self.assertEqual(response.content.decode(), expected_html)
	
	def test_form_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST = {"item": 'A new item',
						"URL":  'A new url',
						"size": 'Item size',
						"color": 'Item color'}

		response = form_page(request)
		content = response.content.decode()
		print(repr(request.POST))

		self.assertIn('A new item', content)
		self.assertIn('A new url', content)
		self.assertIn('Item size', content)
		self.assertIn('Item color', content)
		
class FormModelTest(Testcase):
	def test_saving_and_retrieving_items(self):
		first_item = Form()
		first_item.text = 'First item'
		first_item.save()
		
		second_item = Form()
		second_item.text = 'Second item'
		second_item.save()
		
		third_item = Form()
		third_item.text = 'Third item'
		third_item.save()
		
		fourth_item = Form()
		fourth_item.text = 'Fourth item'
		fourth_item.save()
		
		saved_items = Form.objects.all()
		self.assertEqual(saved_items.count(), 4)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		third_saved_item = saved_items[2]
		fourth_saved_item = save_items[3]
		self.assertEqual(first_saved_item.text,'First item')
		self.assertEqual(second_saved_item.text,'Second item')
		self.assertEqual(third_saved_item.text,'Third item')
		self.assertEqual(fourth_saved_item.text,'Fourth item')
		
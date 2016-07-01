from django.test import TestCase
from line_bot.views import home_page
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
		
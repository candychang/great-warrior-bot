from django.test import TestCase
from line_bot.views import *
from django.core.urlresolvers import resolve
from django.http import HttpRequest
# Create your tests here.
class homeTest(TestCase):
	def test_home_url(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
		
	def test_home_correctect(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<p>Welcome</p>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
		
from behave import *
import line_bot
from line_bot.models import *
from line_bot.factories import RequestFactory

@given(u'I am an admin')
def step_impl(context):
	pass

@when(u'I visit the admin orders page')
def step_impl(context):
    context.browser.visit(context.get_url('admin-orders'))

@then(u'I should see all user orders')
def step_impl(context):
	print(Request.objects.all().count())
	for req in Request.objects.all():
		test_text = req.itemrequest
		context.test.assertTrue(context.browser.is_text_present(test_text))
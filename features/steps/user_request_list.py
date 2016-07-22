from behave import *
from django.core.urlresolvers import reverse
import line_bot
from line_bot.models import *
from line_bot.factories import UserFactory
from line_bot.factories import RequestFactory

@given('there are many users, each with different requests')
def user_setup(context):
	for row in context.table:
		username = row['user']
		item_names = row['requests'].split(', ')
		user = UserFactory(username=username)
		requests = [RequestFactory(itemrequest=n, user=user) for n in item_names]
	print (UserModel.objects.all().count())

@given(u'I am logged in as "{username}"')
def user_login(context, username):
    context.user = UserModel.objects.get(username=username)

@when(u'I visit the orders page')
def visit(context):
	user_id = context.user.id
	context.browser.visit(context.base_url + reverse('orders', args=(user_id,)))

@then(u'I should see all my orders')
def requests_exist(context):
	for req in context.user.request_set.all():
		test_text = req.itemrequest
		context.test.assertTrue(context.browser.is_text_present(test_text))

@then(u'I should not see orders for "{username}"')
def requests_do_not_exist(context, username):
	not_user = UserModel.objects.get(username=username)
	for req in not_user.request_set.all():
		test_text = req.itemrequest
		context.test.assertTrue(context.browser.is_text_not_present(test_text))




from behave import *
from django.core.urlresolvers import reverse
# from line_bot.factories import UserFactory
# from line_bot.factories import Request

@given('there are many users, each with different requests')
def user_setup(context):
    for row in context.table:
        username = row['user']
        item_names = row['requests'].split(', ')
        requests = [Request.objects.get_or_create(item_name__iexact=n) for n in item_names]
        [UserFactory(name=username).request_set.add(req[0]) for req in requests]

@given(u'I am logged in as "{username}"')
def user_login(context, username):
    context.user = UserFactory(name=username)

@when(u'I visit the "{view_name}" page')
def visit(context, view_name):
    context.browser.visit(view_name)

@then(u'I should see all my orders')
def requests_exist(context):
    for req in context.user.request_set.all():
        test_text = req.item_name
        context.test.assertTrue(context.browser.is_text_present(test_text))

@then(u'I should not see orders for "{username}"')
def requests_do_not_exist(context, username):
    not_user = User.objects.get(name__iexact=username)
    for req in context.user.request_set.all():
        test_text = req.item_name
        context.test.assertTrue(context.browser.is_text_not_present(test_text))




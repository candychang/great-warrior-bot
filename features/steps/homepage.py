from behave import *

@when(u'I visit the home page')
def step_impl(context):
    context.browser.visit(context.get_url('home'))

@then(u'I should see "Welcome"')
def step_impl(context):
    context.test.assertTrue(context.browser.is_text_present("Welcome"))

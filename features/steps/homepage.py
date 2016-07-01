from behave import *

@when(u'I visit the home page')
def step_impl(context):
    context.browser.visit('home')

@then(u'I should see "Welcome"')
def step_impl(context):
    context.test.assertTrue(context.browser.is_text_present("Welcome"))

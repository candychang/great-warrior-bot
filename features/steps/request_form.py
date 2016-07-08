from behave import *
import time
@when(u'I fill out this form')
def step_impl(context):
	context.browser.visit(context.get_url('request-form'))
	context.browser.fill('itemrequest','shoes')
	context.browser.fill('url', 'amazon.com')
	context.browser.fill('size', '7')
	context.browser.fill('itemcolor', 'blue')
	context.browser.find_by_css('form input[type=submit]').first.click()
	
	
@then(u'I am redirected to confirmation page')
def step_impl(context):
	context.test.assertEqual(context.browser.url,context.get_url('request-confirm'))
	
	
# @when(u'I don\'t fill the form completely')
# def step_impl(context):
    # # raise NotImplementedError(u'STEP: When I don\'t fill the f

# @then(u'I receive an error message')
# def step_impl(context):
    # # raise NotImplementedError(u'STEP: Then I receive an error

# @given(u'I fill the form incorrectly')
# def step_impl(context):
     # # raise NotImplementedError(u'STEP: Given I fill the form in

# @when(u'I submit the form')
# def step_impl(context):
    # raise NotImplementedError(u'STEP: When I submit the form')
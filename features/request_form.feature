Feature: Request Form
	Request form for orders
	
Scenario: Someone requests shoes
	When I fill out this form
	Then I am redirected to confirmation page
	
| Scenario: Form is incomplete
	| Given I am a user
	| When I don't fill the form completely
	| Then I receive an error message
	
| Scenario: Form has incorrect input
	| Given I am a user
	| But I fill the form incorrectly
	| When I submit the form
	| Then I receive an error message
	
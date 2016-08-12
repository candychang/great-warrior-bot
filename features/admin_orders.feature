Feature: Admin Orders View
	as an admin, I should be able to see all orders
	
Background:
    Given there are many users, each with different requests
    | user                | requests                                      |
    | Celty Sturlson      | cat helmet, scythe                           |
    | Heiwajima Shizuo    | stop sign, vending machine, bartender uniform |

Scenario: Admin sees all requests
    Given I am an admin
    When I visit the admin orders page
    Then I should see all user orders
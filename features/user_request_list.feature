Feature: User's List of Requests
    As a user
    I want to keep track of all my requests
    So that I can better understand my purchase history

Background:
    Given there are many users, each with different requests
    | user                | requests                                      |
    | Celty Sturlson      | cat helment, scythe                           |
    | Heiwajima Shizuo    | stop sign, vending machine, bartender uniform |

Scenario: User sees all requests

    Given I am logged in as "Celty Sturlson"
    When I visit the "request history" page
    Then I should see all my orders
    And I should not see orders for "Heiwajima Shizuo"
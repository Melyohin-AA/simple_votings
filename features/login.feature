@login
Feature: User authentication

  @en
  Scenario: User opens login page
    Given index page is opened
    When I navigate to login page
    Then I verify login page is loaded

  @en
  Scenario: User with valid credentials can log in
    Given login page is opened
    When I try log in as "user1":"pass1"
    Then I verify index page is loaded

  @en
  Scenario: User logs in proper account
    Given logged in as "user1":"pass1"
    When I navigate to profile page
    Then I verify login is proper

  @en
  Scenario Outline: User with invalid password cannot log in
    Given login page is opened
    When I try log in as <login>:<password>
    Then I verify credentials are rejected
    Examples:
      | login    | password |
      | "user1"  | "psas1"  |
      | "user1"  | "paSs1"  |
      | "user1"  | "pass"   |
      | "user1"  | "pass11" |
      | "user1"  | ""       |

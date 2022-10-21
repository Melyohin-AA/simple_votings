Feature: Authentication

  Background: Common steps
    Given Chrome browser is launched (headless="0")
    And server address is "http://127.0.0.1:8000/"

  @login
  Scenario: User with valid credentials can log in
    Given "login/" page is opened
    When I try log in as "'user1'":"'pass1'"
    Then I verify index page is loaded

  @login
  Scenario: User logs in proper account
    Given logged in as "'user1'":"'pass1'"
    When I navigate to profile page
    Then I verify username is proper

  @login
  Scenario Outline: User with invalid password cannot log in
    Given "login/" page is opened
    When I try log in as "<username>":"<password>"
    Then I verify credentials are rejected
    Examples:
      | username | password |
      | 'user1'  | 'psas1'  |
      | 'user1'  | 'paSs1'  |
      | 'user1'  | 'pass'   |
      | 'user1'  | 'pass11' |
      | 'user1'  | ''       |

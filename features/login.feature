Feature: Authentication

  Background: Common steps
    Given Chrome browser is launched (headless="1")

  @login
  Scenario: User with valid credentials can log in
    Given "127.0.0.1:8000" page is opened
    When I try log in as "'admin'":"'admin'"
    Then I verify index page is loaded
    And I close browser

  @login
  Scenario: User logs in proper account
    Given logged in as "'admin'":"'admin'"
    When I navigate to profile page
    Then I verify username is proper
    And I close browser

  @login
  Scenario Outline: User with invalid password cannot log in
    Given "http://www.old.practicalsqa.net/wp-login.php" page is opened
    When I try log in as "<username>":"<password>"
    Then I verify credentials are rejected
    And I close browser
    Examples:
      | username | password |
      | 'admin'  | 'admIn'  |
      | 'admin'  | 'amdin'  |
      | 'admin'  | 'admi'   |
      | 'admin'  | ''       |

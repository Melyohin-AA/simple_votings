Feature: User logout

  @logout
  Scenario: Logged user logs out
    Given logged in as "user1":"pass1"
    When I try to log out
    Then I verify I am not authenticated

#execute in CLI using 'behave features/login.feature'

Feature: Login
    Testing login http://uitestingplayground.com/sampleapp

Scenario: Succesful Login
    Given username and pwd password
    When login in button clicked
    Then show welcome message
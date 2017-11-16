@CRUD
Feature: API
  @scenario_second
  Scenario:
    Given I have connection to "http://todo.ly"
    When I sent GET
    Then I receive status code 200
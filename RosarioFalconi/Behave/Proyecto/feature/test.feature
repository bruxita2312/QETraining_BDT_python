@CRUD
Feature: API
  @scenario_second
  Scenario:
    Given I have connection to "https://www.pivotaltracker.com"
    And on service "/services/v5/me"
    When I sent "58602711c4b125a7d3dc8670e06d8f07"
    Then I receive user token "2a6118f239fa9083cf56206082f3eefe"
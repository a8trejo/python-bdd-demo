Feature: Github API Demo
  Creating test cases for simple requests using the Github API

  @smoke
  Scenario: Get Latest Release
    Given I request the latest release of the "a8trejo/github-demo" repo
    Then I can validate its data

  @regression
  Scenario Outline: Search a PR
    Given I search for <branch_name> in a PR
    Then I can get the PR body
    And status code should be 200
      Examples:
        | branch_name |
        | bug         |
        | auto         |
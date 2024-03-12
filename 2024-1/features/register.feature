# -- FILE: features/register.feature
Feature: Auto-register of a client

  Scenario: A client register by himself
    Given a customer wants to get a bank product
    When he auto register with the API of the bank
    Then the customer will be registered in the database of the bank
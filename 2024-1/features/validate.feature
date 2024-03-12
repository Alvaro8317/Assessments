# -- FILE: features/register.feature
Feature: Validate the profile of a client

  Scenario: A comercial helps the client to get the available products for him
    Given a comercial offer the validation service of the system
    When the customer accepts
    Then the customer will receive all the products that can get of the bank
# -- FILE: features/register.feature
Feature: Modify the data of a client

  Scenario: A comercial helps the client to complement the data of himself
    Given a comercial offer the products of the bank to the customer
    When the comercial use his system to complement the data 
    Then the customer will have all the neccesary data in the database
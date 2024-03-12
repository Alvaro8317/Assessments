# -- FILE: features/steps/modify_steps.py
from behave import given, when, then, step

@given('a comercial offer the products of the bank to the customer')
def step_impl(context):
    pass

@when('the comercial use his system to complement the data')
def step_impl(context):  # -- NOTE: number is converted into integer
    pass

@then('the customer will have all the neccesary data in the database')
def step_impl(context):
    pass
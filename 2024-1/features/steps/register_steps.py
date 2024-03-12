# -- FILE: features/steps/register_steps.py
from behave import given, when, then, step

@given('a customer wants to get a bank product')
def step_impl(context):
    pass

@when('he auto register with the API of the bank')
def step_impl(context):  # -- NOTE: number is converted into integer
    pass

@then('the customer will be registered in the database of the bank')
def step_impl(context):
    pass
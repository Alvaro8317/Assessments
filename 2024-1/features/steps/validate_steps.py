# -- FILE: features/steps/validate_steps.py
from behave import given, when, then, step

@given('a comercial offer the validation service of the system')
def step_impl(context):
    pass

@when('the customer accepts')
def step_impl(context):  # -- NOTE: number is converted into integer
    pass

@then('the customer will receive all the products that can get of the bank')
def step_impl(context):
    pass
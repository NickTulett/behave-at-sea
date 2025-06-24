from behave import *
from features.steps.ui.juice_shop_ui import *
from features.steps.api.juice_shop_api import *

@given("Haxxor goes to the Juice Shop")
def open_juice_shop(context):
    open_shop(context)

@when('she opens the "{}"')
def open_hidden_page(context, page):
    open_page(context, page)

@then('she sees she has solved the "{}" challenge')
def check_challenge(context, challenge_name):
    assert check_challenge_solved(context, challenge_name)

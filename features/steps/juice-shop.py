from behave import *
from features.steps.ui.juice_shop_ui import *

@given("Haxxor goes to the Juice Shop")
def open_juice_shop(context):
    open_shop(context)

@when('she opens the "{}"')
def open_hidden_page(context, page):
    open_page(context, page)

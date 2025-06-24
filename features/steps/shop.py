from behave import *
from features.steps.ui.shop_ui import *

@given("Betty adds items to her basket")
def add_to_basket(context):
    open_shop(context)
    for row in context.table:
        context.selections.append(row)
        for count in range(int(row['Count'])):
            addToBasket(context, row['Item'])

@when('she checks her basket')
def check_basket(context):
    openBasket(context)

@then('she can see her basket contains only her chosen items')
def confirm_basket_contents(context):
    # TODO add subtotal check
    for i in range(len(context.selections)):
        selection = context.selections[i]
        expected_basket_line = selection['Item'] + "Quantity  " + selection['Count'] + "remove" + selection['Price']
        assert expected_basket_line == context.basket_items[i]
base_url = "http://localhost:8080/index.html#/?_k=j71gnu"

def open_shop(context):
    context.page.goto(base_url)

def addToBasket(context, selection):
    itemTitle = context.page.get_by_text(selection)
    itemCard = context.page.locator(".tile").filter(has=itemTitle)
    itemCard.get_by_role("button").click()

def openBasket(context):
    context.basket_items = []
    context.page.get_by_text("Checkout").click()
    for basket_item in context.page.locator(".productItem").all():
        context.basket_items.append(basket_item.text_content())
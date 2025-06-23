from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

@fixture
def browser_page(context):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        context.page = browser.new_page()
        yield context.page
        browser.close()

def before_all(context):
    use_fixture(browser_page, context)
    context.selections = []

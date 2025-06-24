from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
from typing import Generator

@fixture
def browser_page(context):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        context.page = browser.new_page()
        yield context.page
        browser.close()


def before_all(context):
    context.base_url = "https://stc-owasp-juice-dnebatcgf2ddf4cr.uksouth-01.azurewebsites.net"
    context.selections = []
    use_fixture(browser_page, context)

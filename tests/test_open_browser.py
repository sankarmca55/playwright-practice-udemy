import time
from playwright.sync_api import Playwright


def test_open_newBrowser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(3000)
    browser.close()

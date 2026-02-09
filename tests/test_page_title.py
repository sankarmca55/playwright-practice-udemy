import pytest
from playwright.sync_api import Playwright


def test_page_title(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    print(page.title)
    page.wait_for_timeout(3000)
    browser.close()

@pytest.fixture(scope="module")
def test_fixture2(new_data):
    print("test_fixture2")

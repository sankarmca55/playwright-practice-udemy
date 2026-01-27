import time

from playwright.sync_api import Page


def test_playwrightBasics(page:Page):
    page.goto("https://www.google.com")

    try:
        page.get_by_role("button",name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept all")

    page.get_by_role("combobox",name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    time.sleep(5)


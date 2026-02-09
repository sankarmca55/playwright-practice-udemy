import time
from time import sleep

from playwright.sync_api import Page, expect
from pygments.lexer import words


#iphone X , Nokia Edge - We want to add this two iteams to the cart.

def test_UIValidation_DynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # login valid values
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

    time.sleep(5)

def test_childWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_window:
        page.locator(".blinkingText").click()

    childPage = new_window.value

    # Wait for popup page to load
    childPage.wait_for_load_state()

    # Read text from popup
    text = childPage.locator(".red").text_content()
    print(text)
    words = text.split("at")
    email = words[1].strip().split(" ")[0]
    assert email == "mentor@rahulshettyacademy.com"


    time.sleep(5)
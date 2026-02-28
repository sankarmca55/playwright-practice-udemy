import time

from playwright.sync_api import expect


def test_locate(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

#Userdetails
    UserName = page.locator("#user-name")
    UserName.fill("standard_user")
    UserName.click()

    Password = page.locator("#password")
    Password.fill("secret_sauce")
    Password.click()

    page.locator("#login-button").click()

#Adding products to cart
    # locate product
    product = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")

    add_btn = product.get_by_role("button", name="Add to cart")

    expect(add_btn).to_be_visible()
    add_btn.click()
    time.sleep(10)

    product1 = page.locator(".inventory_item").filter(has_text="Sauce Labs Fleece Jacket")

    add_btn1 = product1.get_by_role("button", name="Add to cart")

    expect(add_btn1).to_be_visible()
    add_btn1.click()
    time.sleep(10)

    page.locator("#shopping_cart_container").click()
    time.sleep(10)



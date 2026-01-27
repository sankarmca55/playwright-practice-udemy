
from utils.apiBase import APIutils

from playwright.sync_api import Playwright, expect


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> OrderID
    api_utils = APIutils()
    orderId = api_utils.createOrder(playwright)


    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name ="Login").click()
    print("This is login page")

    page.get_by_role("button", name ="ORDERS").click()

    #Order history page -> Order is visible
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name = "view").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
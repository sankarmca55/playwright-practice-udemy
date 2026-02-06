from playwright.sync_api import Playwright


def test_SimpleLoginAutomation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://in.bookmyshow.com/")
    search_box = page.get_by_placeholder("Search for your city")
    search_box.wait_for()
    search_box.fill("Hyderabad")

    city = page.locator("li:has-text('Hyderabad')").first
    city.wait_for(state="visible")
    city.click()

    page.wait_for_url("**hyderabad**")

    page.wait_for_timeout(3000)
    page.get_by_role("link", name="Movies", exact=True).click()
    page.wait_for_timeout(3000)
    browser.close()
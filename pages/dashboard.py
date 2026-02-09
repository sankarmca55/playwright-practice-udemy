class DashboardPage:
    def __init__(self,page):
        self.page = page

    def DashboardOrderlist(self):
        #self.page.get_by_role("button", name = "ORDERS").click()
        #self.page.get_by_role("button", name="ORDERS").wait_for()
        #self.page.get_by_role("button", name="ORDERS").click()
        self.page.locator("button:has-text('Orders')").click()




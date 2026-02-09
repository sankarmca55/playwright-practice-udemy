from pages.dashboard import DashboardPage



class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        #self.page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        self.page.goto("https://rahulshettyacademy.com/client")

    def userdetails(self,UserName , passWord):
        dashboardpage = DashboardPage(self.page)
        #self.page.get_by_label("email@example.com").fill(UserName)
        #self.page.get_by_label("enter your passsword").fill(passWord)
        self.page.get_by_role("textbox", name="email@example.com").fill(UserName)
        self.page.get_by_role("textbox", name="enter your passsword").fill(passWord)
        self.page.get_by_role("button", name="Login").click()
        return dashboardpage


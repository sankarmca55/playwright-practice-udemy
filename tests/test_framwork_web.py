import time
from time import sleep

import json

import pytest
from playwright.sync_api import Page, expect
from pygments.lexer import words

from pages.dashboard import DashboardPage
from pages.login import LoginPage

with open('testdata/credentials.json') as f:
    test_credentialsdata = json.load(f)
    user_credentials_list = test_credentialsdata['user_credentials']

#iphone X , Nokia Edge - We want to add this two iteams to the cart.

@pytest.mark.parametrize("user_credentials", user_credentials_list)

def test_framwork(page: Page, user_credentials):

    UserName = user_credentials["userName"]
    passWord = user_credentials["password"]
       # print(test_credentials)
    loginPage = LoginPage(page)


    loginPage.navigate()
    dashboardpage = loginPage.userdetails(UserName , passWord)
    dashboardpage.DashboardOrderlist()


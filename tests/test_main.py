import time
import pytest
from playwright.sync_api import Page


def test_playwrightBasics(page:Page):
    page.goto("https://www.google.com")
    
    try:
        page.get_by_role("button",name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept all")

    page.get_by_role("combobox",name="Search").fill("Playwright")
    print("This is new commit")
    page.keyboard.press("Enter")
    time.sleep(5)

def test_python_code(page:Page):
   #dup = [1,1,2,3,4,2,3,4]
   #result = list(set(dup))
   #print(result)
   #sl = [90,67,4,0,5,1,7]
   #sl.sort()
   #print(sl)
   number=[0,8,9,7]
   print(max(number))
   print(Counter("infosys"))



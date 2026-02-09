import pytest
from playwright.sync_api import Playwright
from requests import session


@pytest.fixture(scope="module")
def new_data():
    print("This is first page fixture 1")
    data = 10
    return data

def test_fixture_working(new_data):
    print("This is new page")
    total = new_data + 5
    assert total == 15
    print(f"This is new data value = {total}")

def test_fixture_working1(new_data):
    print("This is new page 2")
    total = new_data + 7
    assert total == 17
    print(f"This is new data value = {total}")
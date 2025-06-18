# tests/test_login_success.py
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_login_success(driver):
    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)
    assert "inventory" in driver.current_url
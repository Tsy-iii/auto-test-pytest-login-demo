import pytest
from pages.login_page import LoginPage

# 数据驱动测试用例
@pytest.mark.parametrize("username, password, expected_msg", [
    ("", "password123", "Epic sadface: Username is required"),
    ("admin", "", "Epic sadface: Password is required"),
    ("wronguser", "wrongpass", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
])
def test_login_fail(driver, username, password, expected_msg):
    page = LoginPage(driver)
    page.load()
    page.login(username, password)
    assert expected_msg in page.get_error_message()

# 单条失败用例测试
def test_login_fail_credentials(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "wrong_pass")
    assert "Epic sadface: Username and password do not match any user in this service" in page.get_error_message()

def test_login_fail_empty_password(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "")
    assert page.get_error_message() == "Epic sadface: Password is required"

def test_login_fail_empyt_username(driver):
    page = LoginPage(driver)
    page.load()
    page.login("", "wrong_pass")
    assert page.get_error_message() == "Epic sadface: Username is required"
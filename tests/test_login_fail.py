# tests/test_login_fail.py
import pytest
from pages.login_page import LoginPage

"""这里是数据驱动的多条用例，可以传入多个参数，并自动生成测试用例"""
@pytest.mark.parametrize("username, password, expected_msg", [
    ("", "password123", "Username cannot be empty"),
    ("admin", "", "Password cannot be empty"),
    ("wronguser", "wrongpass", "Invalid username or password"),
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
])
def test_login_fail(driver, username, password, expected_msg):
    page = LoginPage(driver)
    page.load()
    page.login(username, password)
    # assert page.get_error_message() == expected_msg
    assert expected_msg in page.get_error_msg()
    
"""这里是一条一条的测试用例，测试登录失败的情况"""
def test_login_fail_credentials(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "wrong_pass")
    # assert "inventory" not in driver.current_url
    assert "Invalid username and password" in page.get_error_message()
    
def test_login_fail_empty_password(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wrong_user", "")
    # assert "inventory" not in driver.current_url
    assert page.get_error_message() == "Please enter a password"
    
def test_login_fail_empyt_username(driver):
    page = LoginPage(driver)
    page.load()
    page.login("", "wrong_pass")
    # assert "inventory" not in driver.current_url
    assert page.get_error_message() == "Please enter a username"
    
# tests/test_checkout_validation.py

import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD

@allure.title("测试 Checkout 表单缺失时的错误提示")
@allure.description("参数化多种缺失输入场景，验证错误提示")
@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error", [
    ("", "Xun", "518000", "Error: First Name is required"),
    ("Ye", "", "518000", "Error: Last Name is required"),
    ("Ye", "Xun", "", "Error: Postal Code is required"),
    ("","","", "Error: First Name is required"),
])
def test_checkout_form_validation(driver, first_name, last_name, postal_code, expected_error):
    with allure.step("登录并添加商品"):
        page = LoginPage(driver)
        page.load()
        page.login(USERNAME, PASSWORD)

        inventory = InventoryPage(driver)
        inventory.add_product_to_cart_by_id("sauce-labs-backpack")

        cart = CartPage(driver)
        cart.go_to_cart()

    with allure.step("进入 checkout 页面并填写用户信息"):
        checkout = CheckoutPage(driver)
        checkout.click_checkout_button()
        checkout.fill_user_info(first_name, last_name, postal_code)
        checkout.click_continue()

    with allure.step("断言错误提示是否正确"):
        error_text = checkout.get_error_message()
        assert expected_error in error_text
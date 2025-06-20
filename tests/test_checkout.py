# tests/test_checkout.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD

@allure.title("完整下单流程测试")
@allure.description("标准用户登录后，添加商品到购物车，完成结账，验证成功页面")
def test_complete_checkout_flow(driver):
    with allure.step("登录"):
        page = LoginPage(driver)
        page.load()
        page.login(USERNAME, PASSWORD)

    with allure.step("添加商品"):
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart_by_id("sauce-labs-backpack")

    with allure.step("跳转到购物车页面"):
        cart = CartPage(driver)
        cart.go_to_cart()

    with allure.step("点击 Checkout"):
        checkout = CheckoutPage(driver)
        checkout.click_checkout_button()

    with allure.step("填写用户信息并 Continue"):
        checkout.fill_user_info("Ye", "Xun", "518000")
        checkout.click_continue()

    with allure.step("点击 Finish 完成下单"):
        checkout.click_finish()

    with allure.step("断言下单成功"):
        success_message = checkout.get_success_message()
        assert success_message == "Thank you for your order!"
        
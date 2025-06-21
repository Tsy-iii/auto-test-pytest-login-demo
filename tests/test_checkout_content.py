# tests/test_checkout_content.py

import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from utils.config import USERNAME, PASSWORD

@allure.title("测试订单确认页的商品内容")
@allure.description("验证商品名称与价格是否与添加商品一致")
def test_checkout_overview_content(driver):
    with allure.step("登录"):
        page = LoginPage(driver)
        page.load()
        page.login(USERNAME, PASSWORD)

    with allure.step("添加两个商品"):
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart_by_id("sauce-labs-backpack")
        inventory.add_product_to_cart_by_id("sauce-labs-bike-light")

        expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        
        expected_price_map = {
            "Sauce Labs Backpack": 29.99,
            "Sauce Labs Bike Light": 9.99
        }

    with allure.step("进入购物车并 Checkout"):
        cart = CartPage(driver)
        cart.go_to_cart()

        checkout = CheckoutPage(driver)
        checkout.click_checkout_button()
        checkout.fill_user_info("Ye", "Xun", "518000")
        checkout.click_continue()

    with allure.step("验证订单确认页商品内容"):
        overview = CheckoutOverviewPage(driver)
        actual_items = overview.get_all_product_names()
        assert sorted(actual_items) == sorted(expected_items), f"期望商品：{expected_items}，实际：{actual_items}"
        
    with allure.step("验证总价（含税）"):
        expected_subtotal = sum(expected_price_map.values())
        actual_total = overview.get_total_price()
        # 页面会自动加税，比如 +$3.20
        assert actual_total > expected_subtotal, f"总价应大于商品小计，实际：{actual_total}，商品小计：{expected_subtotal}"
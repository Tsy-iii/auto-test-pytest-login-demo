# tests/test_cart_remove.py

import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USERNAME, PASSWORD

@allure.title("测试购物车中移除商品功能")
@allure.description("添加两个商品后移除一个，验证购物车中只剩一个商品")
def test_remove_item_from_cart(driver):
    with allure.step("登录"):
        page = LoginPage(driver)
        page.load()
        page.login(USERNAME, PASSWORD)

    with allure.step("添加两个商品"):
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart_by_id("sauce-labs-backpack")
        inventory.add_product_to_cart_by_id("sauce-labs-bike-light")

    with allure.step("进入购物车"):
        cart = CartPage(driver)
        cart.go_to_cart()

    with allure.step("移除一个商品"):
        cart.remove_product_by_id("sauce-labs-backpack")

    with allure.step("断言购物车中商品数量为 1"):
        count = cart.get_cart_items_count()
        assert count == 1
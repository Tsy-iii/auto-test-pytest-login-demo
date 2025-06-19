# tests/test_inventory.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import USERNAME, PASSWORD
from pages.cart_page import CartPage

# 添加多个商品到购物车，但是也是一个一个添加。参数化多个商品测试
@pytest.mark.parametrize("product_id", [
    "sauce-labs-backpack",
    "sauce-labs-bike-light",
    "sauce-labs-bolt-t-shirt",
])
def test_add_multiple_products_to_cart(driver, product_id):
    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart_by_id(product_id)

    cart_count = inventory.get_cart_count()
    assert cart_count == "1"

# 添加单个商品到购物车
def test_add_product_to_cart(driver):
    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    cart_count = inventory.get_cart_count()
    assert cart_count == "1"

# 添加2个商品到购物车后，验证购物车图标上的数量是否为2
def test_add_two_products_to_cart_and_check_count(driver):
    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart_by_id("sauce-labs-backpack")
    inventory.add_product_to_cart_by_id("sauce-labs-bike-light")

    cart_count = inventory.get_cart_count()
    assert cart_count == "2"
# 购物车页面包含添加的商品
def test_cart_contains_added_product(driver):
    """
    添加商品后，跳转到购物车页面，断言商品是否真的存在。
    """
    # 1. 登录
    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)

    # 2. 添加商品
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart_by_id("sauce-labs-backpack")

    # 3. 跳转到购物车页面
    cart = CartPage(driver)
    cart.go_to_cart()

    # 4. 获取购物车内商品列表并断言
    items = cart.get_cart_items()
    assert "Sauce Labs Backpack" in items
    
# 添加两个商品后移除其中一个，验证购物车数量变为1
def test_remove_product_from_cart(driver):

    page = LoginPage(driver)
    page.load()
    page.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart_by_id("sauce-labs-backpack")
    inventory.add_product_to_cart_by_id("sauce-labs-bike-light")

    # 移除其中一个商品
    inventory.remove_product_from_cart_by_id("sauce-labs-backpack")

    cart_count = inventory.get_cart_count()
    assert cart_count == "1"
# pages/cart_page.py
from selenium.webdriver.common.by import By

# 断言购物车页面是否真的有该商品

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    """
        点击右上角的购物车图标，跳转到购物车页面。
    """
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    """
        获取购物车页面中所有商品的名称，返回为字符串列表。
    """
    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        # 这是一个列表推导式（list comprehension），将每个商品的名称（即 item.text）收集到一个新的列表中，并返回该列表。
        return [item.text for item in items]
    
    def remove_product_by_id(self, product_id):
        """
        根据商品 ID 移除商品，例如 product_id = "sauce-labs-backpack"
        对应按钮 ID 为：remove-sauce-labs-backpack
        """
        remove_button_id = f"remove-{product_id}"
        self.driver.find_element(By.ID, remove_button_id).click()

    def get_cart_items_count(self):
        """
        获取购物车页面中商品的实际数量
        """
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))
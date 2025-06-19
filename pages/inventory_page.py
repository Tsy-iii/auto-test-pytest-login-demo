# pages/inventory_page.py
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    # 添加商品到购物车（只能添加一个）
    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 添加商品到购物车，通过商品ID
    def add_product_to_cart_by_id(self, product_id):
        """
            f"add-to-cart-{product_id}" 是一个格式化字符串（f-string），用于动态生成元素的 ID 值。
            f 前缀表示这是一个格式化字符串，可以在字符串中嵌入变量。
            {product_id} 是一个占位符，会被实际的 product_id 值替换。
            例如，如果 product_id 是 "sauce-labs-backpack"，
            那么 f"add-to-cart-{product_id}" 将生成字符串 "add-to-cart-sauce-labs-backpack"。
        """
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    # 获取购物车图标上显示的商品数量
    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    # 移除商品（点击 'Remove' 按钮）
    def remove_product_from_cart_by_id(self, product_id):
        remove_button = self.driver.find_element(By.ID, f"remove-{product_id}")
        remove_button.click()
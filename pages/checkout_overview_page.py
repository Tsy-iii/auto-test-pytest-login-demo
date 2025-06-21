# pages/checkout_overview_page.py

from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_all_product_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [el.text for el in elements]

    def get_total_price(self):
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        # 例：'Total: $43.18' → 提取 43.18
        return float(total_text.replace("Total: $", ""))
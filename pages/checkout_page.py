# pages/checkout_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        """
        点击购物车页面的 Checkout 按钮
        """
        self.driver.find_element(By.ID, "checkout").click()

    def fill_user_info(self, first_name, last_name, postal_code):
        """
        填写用户收货信息（必须填写才能继续）
        """
        # self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        # self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        # self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        
        """
        显式等待元素可交互后填写用户信息，避免 ElementNotInteractableException 错误
        """
        wait = WebDriverWait(self.driver, 10)

        # 输入 First Name
        first_input = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_input.clear()
        first_input.send_keys(first_name)

        # 输入 Last Name
        last_input = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_input.clear()
        last_input.send_keys(last_name)

        # 输入 Zip Code
        postal_input = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        postal_input.clear()
        postal_input.send_keys(postal_code)

    def click_continue(self):
        """
        点击 Continue，进入订单确认页面
        """
        self.driver.find_element(By.ID, "continue").click()

    def click_finish(self):
        """
        点击 Finish，完成下单
        """
        self.driver.find_element(By.ID, "finish").click()

    def get_success_message(self):
        """
        获取成功下单页面的确认消息文本（用来断言）
        """
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
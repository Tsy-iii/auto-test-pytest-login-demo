# tests/test_checkout_complete.py
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.config import USERNAME, PASSWORD

@allure.title("测试完整购买流程")
@allure.description("验证用户登录、添加商品、结账并完成订单，最后是否跳转到成功页面并显示成功提示语")
def test_complete_purchase_flow(driver):
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

    with allure.step("断言页面跳转和成功提示"):
        complete = CheckoutCompletePage(driver)
        assert "checkout-complete" in driver.current_url
        assert complete.get_complete_message().lower() == "thank you for your order!"
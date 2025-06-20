import pytest
from selenium import webdriver

# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    
    # 保留你已有的无头模式
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # 有些系统需要加这一句
    options.add_argument('--window-size=1920,1080')

    # 关键：禁用自动填充、密码管理器
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False
    })

    # 创建 WebDriver 实例
    driver = webdriver.Chrome(options=options)
    
    # 设置隐式等待
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

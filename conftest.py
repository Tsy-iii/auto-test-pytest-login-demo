import pytest
from selenium import webdriver
from utils.config import ENABLE_SCREENSHOT  # 推荐放在 config.py 中统一管理
from utils.screenshot_helper import capture_screenshot

# 是否启用失败自动截图
# ENABLE_SCREENSHOT = True  # 设置为 True 可启用截图

@pytest.fixture(scope="function")
def driver(request):
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
    
# pytest hook：保存测试执行阶段的状态（setup/call/teardown）给每个用例加自动截图钩子
# 通过打印日志来验证是否生效，来定位错误，判断hook是否生效
# 这段代码是hook的标准模版，必须加hookwrapper=True，否则yield不生效
# 统一 hook，失败截图逻辑
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and ENABLE_SCREENSHOT:
        driver = item.funcargs.get("driver")
        if driver:
            print(f"📸 捕获失败测试：{item.name}")
            capture_screenshot(driver, name=item.name)

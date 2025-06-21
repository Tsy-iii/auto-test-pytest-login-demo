import pytest
from selenium import webdriver
from utils.screenshot_helper import capture_screenshot

# 是否启用失败自动截图
ENABLE_SCREENSHOT = False  # 设置为 True 可启用截图

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
    
    print("➡️ yield 后开始判断 rep_call 是否存在")
    # 这里用 getattr 防止异常
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        print(f"📸 测试失败，准备截图: {request.node.name}")
        capture_screenshot(driver, name=request.node.name)
    else:
        print("❌ rep_call 不存在或测试未失败")

    # 如果测试失败，自动截图
    if request.node.rep_call.failed:
        capture_screenshot(driver, name=request.node.name)
    
    driver.quit()
    
# pytest hook：保存测试执行阶段的状态（setup/call/teardown）给每个用例加自动截图钩子
# 通过打印日志来验证是否生效，来定位错误，判断hook是否生效

# 这段代码是hook的标准模版，必须加hookwrapper=True，否则yield不生效
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     print("✅ pytest_runtest_makereport 被执行了")
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and ENABLE_SCREENSHOT:
        driver = item.funcargs.get("driver")
        if driver:
            from utils.screenshot_helper import capture_screenshot
            capture_screenshot(driver, item.name)

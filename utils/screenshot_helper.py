# utils/screenshot_helper.py

import allure
import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 用来统一封装截图 + 添加到 Allure 的方法
def capture_screenshot(driver, name="screenshot"):
    try:
        # 等待一个页面上的稳定元素出现（你可以换成适合你的）
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))  # 适配 saucedemo
        )
    except Exception as e:
        print(f"⚠️ 元素等待失败: {e}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join("screenshots", filename)

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.save_screenshot(screenshot_path)

    with open(screenshot_path, "rb") as image_file:
        allure.attach(image_file.read(), name, attachment_type=allure.attachment_type.PNG)

'''----------------------------------------------'''
# import time
# # 不是最佳方式，截图前强制 time.sleep(1) 看是否能解决截图空白问题：
# def capture_screenshot(driver, name="screenshot"):
#     time.sleep(1)
#     filepath = f"screenshots/{name}.png"
#     driver.save_screenshot(filepath)

'''----------------------------------------------'''
# 终极解决方案：使用 devtools 截图（非 save_screenshot）
# save_screenshot() 是传统截图方式，但在无头模式下不稳定。
# 你可以改用 Chrome DevTools 协议（CDP） 截图方式，更加真实可靠：

# import base64
# import os
# from datetime import datetime
# import allure

# def capture_screenshot(driver, name="screenshot"):
#     try:
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{name}_{timestamp}.png"
#         screenshot_path = os.path.join("screenshots", filename)

#         if not os.path.exists("screenshots"):
#             os.makedirs("screenshots")

#         # 使用 DevTools 协议截图（返回 base64）
#         screenshot_base64 = driver.execute_cdp_cmd("Page.captureScreenshot", {})["data"]

#         # 保存为文件
#         with open(screenshot_path, "wb") as f:
#             f.write(base64.b64decode(screenshot_base64))

#         # 添加到 Allure 报告
#         with open(screenshot_path, "rb") as image_file:
#             allure.attach(image_file.read(), name, attachment_type=allure.attachment_type.PNG)

#         print(f"✅ 使用 DevTools 成功截图: {screenshot_path}")
#     except Exception as e:
#         print(f"❌ 截图失败: {e}")
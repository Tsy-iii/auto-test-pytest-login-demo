# 🧪 Pytest + Selenium 自动化测试项目（基于 saucedemo.com）

这是一个使用 `Pytest + Selenium` 实现的电商网站自动化测试项目，基于公开测试站点 [saucedemo.com](https://www.saucedemo.com/)，模拟用户从登录、商品添加、购物车校验、信息填写、订单完成等核心流程，适合作为自动化测试开发入门与简历展示项目。

---

## 📚 技术栈与特性

- ✅ Python 3.10+
- ✅ Selenium + Pytest
- ✅ Allure 报告集成
- ✅ Page Object 页面封装模式
- ✅ 支持自动截图（失败场景）
- ✅ Git 版本控制 / GitHub 项目管理

---

## 🗂 项目结构

```text
AutoTestFramework/
├── pages/                     # 页面对象封装层（PO 模式）
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/                     # 测试用例层
│   ├── test_login_success.py
│   ├── test_login_fail.py
│   ├── test_inventory.py
│   ├── test_cart_remove.py
│   ├── test_checkout.py
│   ├── test_checkout_content.py
│   ├── test_checkout_validation.py
│   └── test_checkout_complete.py
│
├── utils/                     # 工具模块
│   ├── config.py              # 配置项（用户名、密码、开关等）
│   └── screenshot_helper.py  # 截图封装
│
├── conftest.py                # 公共 fixture 管理、driver 启动与 hook 钩子
├── requirements.txt           # 项目依赖包列表
├── README.md                  # 项目说明文档（你正在看的）
├── screenshots/               # 失败截图输出目录
└── allure-results/            # Allure 报告结果目录
```

## 🚀 快速开始

### 安装依赖

pip install -r requirements.txt

### 执行测试并生成报告数据

pytest --alluredir=allure-results

### 打开 Allure 报告

allure serve allure-results

---

## ✅ 已完成用例一览

| 模块       | 用例说明                                       |
|------------|------------------------------------------------|
| 登录       | 正确登录、错误登录、空账号/空密码校验         |
| 商品       | 添加商品、移除商品、验证购物车数量与信息       |
| 购物车     | 继续购物、继续结账、跳转校验                   |
| 结账       | 填写用户信息、校验为空时提示、继续按钮跳转     |
| 确认订单   | 校验商品内容、订单总价、完成跳转               |

---

## 📸 自动截图说明

- 开启方式：在 conftest.py 中设置 ENABLE_SCREENSHOT = True
- 默认保存在 /screenshots/ 目录
- 失败用例自动截图，并集成进 Allure 报告中

---

## 💡 可扩展方向

- 封装 BasePage 通用方法（click、send_keys 等）
- 接入 CI 流水线（GitHub Actions）
- 使用 yaml/json 管理测试数据
- 接入日志模块 logging 输出测试日志

---

## 👤 项目信息

- **作者**：叶树潭（Shutan Ye）  
- **城市**：深圳  
- **GitHub**：[Tsy-iii](https://github.com/Tsy-iii)

## 📌 声明

本项目仅用于学习与作品集展示，测试站点为公开测试网站 saucedemo.com，无商业用途。
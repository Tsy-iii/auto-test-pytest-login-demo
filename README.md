project_root/
├── conftest.py               # Pytest 配置，如 fixture 定义
├── requirements.txt          # 所需库（如 selenium、pytest、allure-pytest）
├── pages/
│   └── login_page.py         # 页面对象模型（封装登录页面操作）
├── tests/
│   ├── test_login_success.py # 登录成功测试用例
│   └── test_login_fail.py    # 登录失败测试用例
├── utils/
│   └── config.py             # 存放配置，如账号密码等
└── README.md                 # 项目说明文档

# README.md
# SauceDemo Pytest + Page Object 自动化测试项目

## 说明
基于 pytest + selenium + page object 封装的自动化测试项目。

测试站点：[https://www.saucedemo.com](https://www.saucedemo.com)

## 运行方式
1. 安装依赖：`pip install -r requirements.txt`
2. 运行测试：`pytest tests/`
3. 生成报告：`pytest --alluredir=./allure-results`
4. 打开报告：`allure serve ./allure-results`

## 测试用例
- 登录成功
- 登录失败（错误账号）
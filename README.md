# 🧪 Auto Test Project: Pytest + Selenium Login Demo

This is a demo project for automated UI login testing using **Selenium**, **Pytest**, and **Page Object Model** architecture.  
The test cases are designed for [https://www.saucedemo.com/](https://www.saucedemo.com/) and can be used as a reference for beginners or job interview portfolios.

---

## ✅ Features

- Page Object Model structure
- Pytest test framework
- Allure report support
- Valid login test
- Invalid login scenarios (empty username/password, locked user, etc.)
- Parameterized tests

---

## 🧰 Tech Stack

- Python 3.10
- Selenium
- Pytest
- Allure-pytest
- Git & GitHub

---

## 📷 Allure Report Preview

<img src="screenshots/allure-sample.png" width="800"/>

> You can generate the Allure report locally using:
>
> ```bash
> pytest --alluredir=allure-results
> allure serve allure-results
> ```

---

## 🔧 How to Run

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
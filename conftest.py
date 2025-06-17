import pytest
import allure
from selenium import webdriver
from data import LOGIN_PAGE_URL, FORGOT_PASSWORD_PAGE_URL


@allure.title("Открываем браузер и переходим на страницу Логин")
@pytest.fixture(params=["chrome", "firefox"])
#@pytest.fixture(params=["firefox"])
def driver_login_page(request):
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()
    driver.get(LOGIN_PAGE_URL)
    yield driver
    driver.quit()

@allure.title("Открываем браузер и переходим на страницу Восстановление пароля")
@pytest.fixture(params=["chrome", "firefox"])
#@pytest.fixture(params=["firefox"])
def driver_forgot_password_page(request):
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()
    driver.get(FORGOT_PASSWORD_PAGE_URL)
    yield driver
    driver.quit()

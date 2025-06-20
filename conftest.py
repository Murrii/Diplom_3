import pytest
import allure
from selenium import webdriver
from data import LOGIN_PAGE_URL, FORGOT_PASSWORD_PAGE_URL
from pages.login_page import LoginPage
import config


@allure.title("Открываем браузер и переходим на страницу Логин")
@pytest.fixture(params=["chrome", "firefox"])
#@pytest.fixture(params=["firefox"])
def driver_login_page(request):
    driver = None
    if request.param == "firefox":
        config.browser = "firefox"
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        config.browser = "chrome"
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
        config.browser = "firefox"
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        config.browser = "chrome"
        driver = webdriver.Chrome()
    driver.get(FORGOT_PASSWORD_PAGE_URL)
    yield driver
    driver.quit()

@allure.title("Открываем браузер и авторизируемся")
@pytest.fixture(params=["chrome", "firefox"])
#@pytest.fixture(params=["firefox"])
#@pytest.fixture(params=["chrome"])
def driver_auth_main_page(request):
    driver = None
    if request.param == "firefox":
        config.browser = "firefox"
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        config.browser = "chrome"
        driver = webdriver.Chrome()


    # Открываем экран авторизации и авторизируемся
    driver.get(LOGIN_PAGE_URL)
    login_page = LoginPage(driver)
    login_page.login()
    yield driver
    driver.quit()
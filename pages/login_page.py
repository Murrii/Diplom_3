from pages.base_page import BasePage
from locators import login_page_locators
from data import LOGIN_EMAIL as EMAIL, LOGIN_PASSWORD as PASSWORD
import allure


class LoginPage(BasePage):
    @allure.step("Авторизируемся в системе")
    def login(self):
        email_field = self.find_element_with_wait_clickable(login_page_locators.EMAIL_INPUT)
        self.click_on_element(email_field)
        self.fill_text_to_field(email_field, EMAIL)
        password_field = self.find_element_with_wait_clickable(login_page_locators.PASS_INPUT)
        self.click_on_element(password_field)
        self.fill_text_to_field(password_field, PASSWORD)
        self.click_on_element(login_page_locators.LOGIN_BUTTON)
        self.find_element_with_wait_clickable(login_page_locators.GET_FOOD_BUTTON)
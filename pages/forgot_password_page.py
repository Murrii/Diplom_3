import allure
from pages.base_page import BasePage
from locators import forgot_password_page_locators
from data import EMAIL


class ForgotPasswordPage(BasePage):
    @allure.step("Вводим емейл в поле ввода емейла")
    def enter_email(self):
        self.find_element_with_wait_clickable(forgot_password_locators.MAIL_TEXT_FIELD_LOCATOR)
        self.click_on_element(forgot_password_locators.MAIL_TEXT_FIELD_LOCATOR)
        self.fill_text_to_field(forgot_password_locators.MAIL_TEXT_FIELD_LOCATOR, EMAIL)

    @allure.step("Кликаем на кнопку 'Восстановить' на экране 'Восстановление пароля'")
    def click_on_reset_button(self):
        self.find_element_with_wait_clickable(forgot_password_locators.RESET_BUTTON_LOCATOR)
        self.click_on_element(forgot_password_locators.RESET_BUTTON_LOCATOR)
        self.find_element_with_wait_clickable(forgot_password_locators.RESET_PASSWORD_FIELD_LOCATOR)

    @allure.step("Кликаем на кнопку 'Забыли пароль?' на экране 'Логин'")
    def click_on_open_reset_button_page_button(self):
        self.find_element_with_wait_clickable(forgot_password_locators.OPEN_RESET_PASSWORD_PAGE_BUTTON_LOCATOR)
        self.click_on_element(forgot_password_locators.OPEN_RESET_PASSWORD_PAGE_BUTTON_LOCATOR)
        self.find_element_with_wait_visibility(forgot_password_locators.RESET_BUTTON_LOCATOR)

    @allure.step("Получаем текст кнопки Восстановить / Сохранить на экране forgot-password / reset-password")
    def get_text_from_reset_button(self):
        return self.get_text_from_element(forgot_password_locators.RESET_BUTTON_LOCATOR)

    @allure.step("Находим подсвеченное поле и возвращаем его текст")
    def get_text_from_active_field(self):
        active_element = self.find_element_with_wait_visibility(forgot_password_locators.PASSWORD_TEXT_FIELD_FOCUSED_LOCATOR)
        return active_element.text

    @allure.step("Кликаем на иконку глаза на экране /reset-password")
    def click_on_eye_icon_button(self):
        self.find_element_with_wait_clickable(forgot_password_locators.EYE_ICON_LOCATOR)
        self.click_on_element(forgot_password_locators.EYE_ICON_LOCATOR)
import allure
from pages.forgot_password_page import ForgotPasswordPage
from data import RESET_BUTTON_LOCATOR_TEXT, SAVE_RESET_BUTTON_LOCATOR_TEXT, PASSWORD_TEXT_FIELD_FOCUSED_PLACEHOLDER_TEXT


class TestForgotPasswordPage:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_open_reset_password_page_button_jump_to_reset_password_page(self, driver_login_page):
        page = ForgotPasswordPage(driver_login_page)
        page.click_on_open_reset_page_button()
        assert page.get_text_from_reset_button() == RESET_BUTTON_LOCATOR_TEXT

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_reset_button_jump_to_next_page(self, driver_forgot_password_page):
        page = ForgotPasswordPage(driver_forgot_password_page)
        page.enter_email()
        page.click_on_reset_button()
        assert page.get_text_from_reset_button() == SAVE_RESET_BUTTON_LOCATOR_TEXT

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_on_eye_button_is_made_password_field_active(self, driver_forgot_password_page):
        page = ForgotPasswordPage(driver_forgot_password_page)
        page.enter_email()
        page.click_on_reset_button()
        page.click_on_eye_icon_button()
        assert page.get_text_from_active_field() == PASSWORD_TEXT_FIELD_FOCUSED_PLACEHOLDER_TEXT


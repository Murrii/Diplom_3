from pages.profile_page import ProfilePage
from data import EXIT_BUTTON_TEXT, ORDERS_HISTORY_TEXT, OPEN_FORGOT_PASSWORD_PAGE_BUTTON_TEXT
import allure
from pages.forgot_password_page import ForgotPasswordPage


class TestProfilePage:
    @allure.title("Переход по клику на «Личный кабинет»")
    def test_click_personal_account_button_jump_to_profile_page(self, driver_auth_main_page):
        page = ProfilePage(driver_auth_main_page)
        page.go_to_the_profile()
        assert page.get_text_from_exit_button() == EXIT_BUTTON_TEXT

    @allure.title("Переход в раздел «История заказов»")
    def test_click_history_button_jump_to_orders_history_page(self, driver_auth_main_page):
        page = ProfilePage(driver_auth_main_page)
        page.go_to_the_profile()
        page.go_to_the_orders_history()
        assert page.get_active_tab_name() == ORDERS_HISTORY_TEXT

    @allure.title("Выход из аккаунта")
    def test_click_on_exit_button_logout(self, driver_auth_main_page):
        profile_page = ProfilePage(driver_auth_main_page)
        profile_page.go_to_the_profile()
        profile_page.click_on_exit_button()
        login_page = ForgotPasswordPage(driver_auth_main_page)
        assert login_page.get_text_from_open_reset_page_button() == OPEN_FORGOT_PASSWORD_PAGE_BUTTON_TEXT

from pages.base_page import BasePage
from locators import profile_page_locators
from locators import forgot_password_page_locators    # локатор для ожидания загрузки страницы при выходе
import allure


class ProfilePage(BasePage):
    @allure.step("Нажимаем на кнопку 'Личный кабинет'")
    def go_to_the_profile(self):
        profile_button = self.find_element_with_wait_clickable(profile_page_locators.PERSONAL_ACCOUNT_BUTTON_LOCATOR)
        self.click_on_element(profile_button)
        # ждем, пока прогрузится страница профиля
        self.find_element_with_wait_clickable(profile_page_locators.EXIT_BUTTON_LOCATOR)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_on_exit_button(self):
        exit_button = self.find_element_with_wait_clickable(profile_page_locators.EXIT_BUTTON_LOCATOR)
        self.click_on_element(exit_button)
        # ждем, пока прогрузится экран авторизации
        self.find_element_with_wait_clickable(forgot_password_page_locators.OPEN_RESET_PASSWORD_PAGE_BUTTON_LOCATOR)

    @allure.step("Получаем текст кнопки 'Выход'")
    def get_text_from_exit_button(self):
        return self.get_text_from_element(profile_page_locators.EXIT_BUTTON_LOCATOR)

    @allure.step("Нажимаем на кнопку 'История заказов'")
    def go_to_the_orders_history(self):
        history_button = self.find_element_with_wait_clickable(profile_page_locators.HISTORY_BUTTON_LOCATOR)
        self.click_on_element(history_button)
        # ждем, пока прогрузится страница Истории заказов
        self.find_element_with_wait_visibility(profile_page_locators.ORDER_HISTORY_LIST_LOCATOR)

    @allure.step("Получаем имя активной вкладки")
    def get_active_tab_name(self):
        # ждем, чтобы элемент отобразился на странице и возвращаем его текст
        self.find_element_with_wait_visibility(profile_page_locators.ACTIVE_TAB_LOCATOR)
        return self.get_text_from_element(profile_page_locators.ACTIVE_TAB_LOCATOR)

import allure
from pages.base_page import BasePage
from locators import main_page_locators
from config import browser


class MainPage(BasePage):
    @allure.step("Нажимаем на кнопку Конструктор")
    def click_on_constructor_button(self):
        self.click_on_element(main_page_locators.CONSTRUCTOR_BUTTON_LOCATOR)
        self.find_element_with_wait_clickable(main_page_locators.BUN_INGREDIENT_LOCATOR)

    @allure.step("Получаем имя тестового ингредиента")
    def get_ingredient_name(self):
        return self.get_text_from_element(main_page_locators.BUN_INGREDIENT_LOCATOR)

    @allure.step("перетаскиваем ингредиент в заказ")
    def drag_ingredient_to_order(self):
        if browser == "chrome":
            self.drag_from_drop_to_chrome(main_page_locators.BUN_INGREDIENT_LOCATOR, main_page_locators.ORDER_SECTION_LOCATOR)
        elif browser == "firefox":
            self.drag_from_drop_to_firefox(main_page_locators.BUN_INGREDIENT_LOCATOR, main_page_locators.ORDER_SECTION_LOCATOR)

    @allure.step("Получаем значение счетчика")
    def get_counter_value(self):
        # ждем, пока элемент загрузится
        self.find_element_with_wait_clickable(main_page_locators.COUNTER_ICON_LOCATOR)
        # возвращаем текст элемента в формате int
        return int(self.get_text_from_element(main_page_locators.COUNTER_ICON_LOCATOR))

    @allure.step("Нажимаем на ингредиент")
    def click_on_ingredient(self):
        ingredient = self.find_element_with_wait_clickable(main_page_locators.BUN_INGREDIENT_LOCATOR)
        self.click_on_element(ingredient)

    @allure.step("Получаем заголовок модального окна")
    def get_modal_window_title_text(self):
        self.find_element_with_wait_visibility(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)
        return self.get_text_from_element(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)

    @allure.step("Проверяем, что модальное окно скрыто")
    def is_modal_window_invisible(self):
        return self.is_element_invisible(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)

    @allure.step("Закрываем модальное окно с деталями ингредиента")
    def close_modal_window_details(self):
        close_button = self.find_element_with_wait_clickable(main_page_locators.CLOSE_MODAL_WINDOW_DETAILS_BUTTON_LOCATOR)
        self.click_on_element(close_button)

    @allure.step("Закрываем модальное окно с деталями заказа")
    def close_modal_window_order(self):
        close_button = self.find_element_with_wait_clickable(main_page_locators.CLOSE_MODAL_WINDOW_ORDER_BUTTON_LOCATOR)
        self.click_on_element(close_button)

    @allure.step("Добавляем ингредиент и нажимаем на кнопку создания заказа")
    def click_on_make_order_button(self):
        self.drag_ingredient_to_order()
        order_button = self.find_element_with_wait_clickable(main_page_locators.MAKE_ORDER_BUTTON_LOCATOR)
        self.click_on_element(order_button)
        self.find_element_with_wait_visibility(main_page_locators.ORDER_ID_LOCATOR)

    @allure.step("получаем id заказа")
    def get_order_id(self):
        return int(self.get_text_from_element(main_page_locators.ORDER_ID_LOCATOR))

    @allure.step("Создаем новый заказ")
    def make_order_return_id(self):
        self.click_on_make_order_button()
        self.check_order_id_is_changed()
        self.close_modal_window_order()
        return self.get_order_id()

    @allure.step("Проверяем, что id заказа изменился с дефолтного на настоящий")
    def check_order_id_is_changed(self):
        self.wait_change_of_element(main_page_locators.ORDER_ID_LOCATOR, 9999)
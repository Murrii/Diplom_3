from pages.base_page import BasePage
from locators import main_page_locators
from config import browser


class MainPage(BasePage):
    def click_on_constructor_button(self):
        self.click_on_element(main_page_locators.CONSTRUCTOR_BUTTON_LOCATOR)
        self.find_element_with_wait_clickable(main_page_locators.BUN_INGREDIENT_LOCATOR)

    def get_ingredient_name(self):
        return self.get_text_from_element(main_page_locators.BUN_INGREDIENT_LOCATOR)

    def drag_ingredient_to_order(self):
        if browser == "chrome":
            self.drag_from_drop_to_chrome(main_page_locators.BUN_INGREDIENT_LOCATOR, main_page_locators.ORDER_SECTION_LOCATOR)
        elif browser == "firefox":
            self.drag_from_drop_to_firefox(main_page_locators.BUN_INGREDIENT_LOCATOR, main_page_locators.ORDER_SECTION_LOCATOR)

    def get_counter_value(self):
        # ждем, пока элемент загрузится
        self.find_element_with_wait_clickable(main_page_locators.COUNTER_ICON_LOCATOR)
        # возвращаем текст элемента в формате int
        return int(self.get_text_from_element(main_page_locators.COUNTER_ICON_LOCATOR))

    def click_on_ingredient(self):
        ingredient = self.find_element_with_wait_clickable(main_page_locators.BUN_INGREDIENT_LOCATOR)
        self.click_on_element(ingredient)

    def get_modal_window_title_text(self):
        self.find_element_with_wait_visibility(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)
        return self.get_text_from_element(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)

    def is_modal_window_invisible(self):
        return self.is_element_invisible(main_page_locators.MODAL_WINDOW_TITLE_LOCATOR)

    def close_modal_window_ingredient(self):
        close_button = self.find_element_with_wait_clickable(main_page_locators.CLOSE_MODAL_WINDOW_BUTTON_LOCATOR)
        self.click_on_element(close_button)

    def make_order(self):
        self.drag_ingredient_to_order()
        order_button = self.find_element_with_wait_clickable(main_page_locators.MAKE_ORDER_BUTTON_LOCATOR)
        self.click_on_element(order_button)
        self.find_element_with_wait_visibility(main_page_locators.ORDER_ID_LOCATOR)

    def get_order_id(self):
        self.make_order()
        return int(self.get_text_from_element(main_page_locators.ORDER_ID_LOCATOR))

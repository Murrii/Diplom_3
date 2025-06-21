from pages.base_page import BasePage
import allure
from locators import feed_page_locators

class FeedPage(BasePage):
    @allure.step("Нажимаем на последний созданный заказ")
    def click_on_feed_last_order(self):
        try:
            order = self.find_element_with_wait_clickable(feed_page_locators.FEED_ORDERS_LOCATOR)
            self.click_on_element(order)
        except TimeoutError:
            print("В ленте нет заказов")

    @allure.step("Нажимаем на кнопку Лента заказов")
    def click_on_feed_button(self):
        feed_button = self.find_element_with_wait_clickable(feed_page_locators.FEED_BUTTON_LOCATOR)
        self.click_on_element(feed_button)

    @allure.step("Получаем заголовок модального окна создания заказа")
    def get_order_status_finished_title_text(self):
        self.find_element_with_wait_visibility(feed_page_locators.ORDER_STATUS_FINISHED_TITLE_LOCATOR)
        return self.get_text_from_element(feed_page_locators.ORDER_STATUS_FINISHED_TITLE_LOCATOR)

    @allure.step("Проверяем, что отображается модальное окно заказа")
    def is_order_modal_window_visible(self):
        return self.is_element_visible(feed_page_locators.MODAL_WINDOW_ORDER_INFO_LOCATOR)

    @allure.step("Получаем список заказов")
    def get_list_of_orders_id(self):
        self.find_element_with_wait_visibility(feed_page_locators.FEED_ORDERS_IDS_LOCATOR)
        list_of_orders = self.get_list_of_elements(feed_page_locators.FEED_ORDERS_IDS_LOCATOR)
        list_of_orders_id = []
        for order in list_of_orders:
            order_id = self.get_text_from_element_without_locator(order)
            list_of_orders_id.append(order_id)
        return list_of_orders_id

    @allure.step("Получаем значения счетчиков заказов")
    def get_values_of_order_counters(self):
        self.find_element_with_wait_visibility(feed_page_locators.ORDER_COUNTERS_VALUES_LOCATOR)
        list_of_elements = self.get_list_of_elements(feed_page_locators.ORDER_COUNTERS_VALUES_LOCATOR)
        counters_list = []
        for element in list_of_elements:
            value = self.get_text_from_element_without_locator(element)
            counters_list.append(value)
        return counters_list

    @allure.step("Получаем значение счетчика заказов за все время")
    def get_counter_all_orders_value(self):
        list_of_values = self.get_values_of_order_counters()
        return list_of_values[0]

    @allure.step("Получаем значение счетчика заказов за сегодня")
    def get_counter_today_orders_value(self):
        list_of_values = self.get_values_of_order_counters()
        return list_of_values[1]

    @allure.step("Получаем список заказов в работе")
    def get_list_of_orders_in_work(self):
        self.find_element_with_wait_visibility(feed_page_locators.ORDERS_IN_WORK_LIST_LOCATOR)
        list_of_orders = self.get_list_of_elements(feed_page_locators.ORDERS_IN_WORK_LIST_LOCATOR)
        list_ids_orders_in_work = []
        for order in list_of_orders:
            order_id = self.get_text_from_element_without_locator(order)
            list_ids_orders_in_work.append(order_id)
        return list_ids_orders_in_work

    @allure.step("Ждем, пока новый заказ отобразится в списке заказов в работе")
    def wait_for_adding_order_id_in_work_list(self, text):
        try:
            self.wait_text_is_visible(feed_page_locators.ORDERS_IN_WORK_LIST_LOCATOR, text)
        except TimeoutError:
            pass

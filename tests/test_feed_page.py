from pages.feed_page import FeedPage
from pages.main_page import MainPage
import allure
from data import ORDER_STATUS_FINISHED_TITLE


class TestFeedPage:
    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_on_feed_button_jump_to_feed_page(self, driver_auth_main_page):
        page = FeedPage(driver_auth_main_page)
        page.click_on_feed_button()
        assert page.get_order_status_finished_title_text() == ORDER_STATUS_FINISHED_TITLE

    @allure.title("Клик на заказе открывает всплывающее окно с деталями")
    def test_click_on_order_open_modal_window_order_details(self, driver_auth_feed_page):
        page = FeedPage(driver_auth_feed_page)
        page.click_on_feed_last_order()
        assert page.is_order_modal_window_visible()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_feed_include_new_order_true(self, driver_auth_main_page):
        order_page = MainPage(driver_auth_main_page)
        order_id = '#0' + str(order_page.make_order_return_id())
        feed_page = FeedPage(driver_auth_main_page)
        feed_page.click_on_feed_button()
        assert order_id in feed_page.get_list_of_orders_id()

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_all_orders_counter_value_grow_when_new_order_added_true(self, driver_auth_feed_page):
        feed_page = FeedPage(driver_auth_feed_page)
        old_counter_value = feed_page.get_counter_all_orders_value()
        main_page = MainPage(driver_auth_feed_page)
        main_page.click_on_constructor_button()
        main_page.make_order_return_id()
        feed_page.click_on_feed_button()
        new_counter_value = feed_page.get_counter_all_orders_value()
        assert new_counter_value > old_counter_value, (
            print('old_counter_value is', old_counter_value, ", new_counter_value is", new_counter_value))

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_orders_counter_value_grow_when_new_order_added_true(self, driver_auth_feed_page):
        feed_page = FeedPage(driver_auth_feed_page)
        old_counter_value = feed_page.get_counter_today_orders_value()
        main_page = MainPage(driver_auth_feed_page)
        main_page.click_on_constructor_button()
        main_page.make_order_return_id()
        feed_page.click_on_feed_button()
        new_counter_value = feed_page.get_counter_today_orders_value()
        assert new_counter_value > old_counter_value, (
            print('old_counter_value is', old_counter_value, ", new_counter_value is", new_counter_value))

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_feed_of_orders_in_work_include_new_order_id(self, driver_auth_main_page):
        main_page = MainPage(driver_auth_main_page)
        # приводим формат id в соответствие с форматом в списке заказов
        order_id = "0" + str(main_page.make_order_return_id())
        feed_page = FeedPage(driver_auth_main_page)
        feed_page.click_on_feed_button()
        feed_page.wait_for_adding_order_id_in_work_list(order_id)
        orders_in_work = feed_page.get_list_of_orders_in_work()
        assert order_id in orders_in_work, print("order_id is", order_id, ", orders_in_work is", orders_in_work)


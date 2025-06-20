from pages.main_page import MainPage
from data import BUN_INGREDIENT_NAME_TEXT, DETAIL_MODAL_WINDOW_TITLE
import allure


class TestMainPage:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_on_constructor_button_jump_to_main_page(self, driver_forgot_password_page):
        page = MainPage(driver_forgot_password_page)
        page.click_on_constructor_button()
        assert page.get_ingredient_name() == BUN_INGREDIENT_NAME_TEXT

    @allure.title("Клик на ингредиенте открывает всплывающее окно с деталями")
    def test_click_on_ingredient_open_modal_window(self, driver_auth_main_page):
        page = MainPage(driver_auth_main_page)
        page.click_on_ingredient()
        assert page.get_modal_window_title_text() == DETAIL_MODAL_WINDOW_TITLE

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_on_close_button_detail_modal_window_close(self, driver_auth_main_page):
        page = MainPage(driver_auth_main_page)
        page.click_on_ingredient()
        page.close_modal_window_ingredient()
        assert page.is_modal_window_invisible()

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_add_ingredient_in_order_increase_counter(self, driver_auth_main_page):
        page = MainPage(driver_auth_main_page)
        start_value = page.get_counter_value()
        page.drag_ingredient_to_order()
        finish_value = page.get_counter_value()
        assert finish_value > start_value

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_auth_user_make_order_open_order_modal_window(self, driver_auth_main_page):
        page = MainPage(driver_auth_main_page)
        page.drag_ingredient_to_order()
        page.make_order()
        order_id_number = page.get_order_id()
        # проверяем, что отобразился id заказа
        assert order_id_number > 0
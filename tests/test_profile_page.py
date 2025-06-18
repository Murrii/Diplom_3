from pages.profile_page import ProfilePage
from data import EXIT_BUTTON_TEXT


class TestProfilePage:
    def test_click_personal_account_button_jump_to_profile_page(self, driver_auth_main_page):
        page = ProfilePage(driver_auth_main_page)
        page.go_to_the_profile()
        assert page.get_text_from_exit_button() == EXIT_BUTTON_TEXT

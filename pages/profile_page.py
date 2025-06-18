from pages.base_page import BasePage
from locators import profile_page_locators


class ProfilePage(BasePage):
    def go_to_the_profile(self):
        profile_button = self.find_element_with_wait_clickable(profile_page_locators.PERSONAL_ACCOUNT_BUTTON)
        profile_button.click()
        # ждем, пока прогрузится страница профиля
        self.find_element_with_wait_clickable(profile_page_locators.EXIT_BUTTON_LOCATOR)

    def get_text_from_exit_button(self):
        return self.get_text_from_element(profile_page_locators.EXIT_BUTTON_LOCATOR)
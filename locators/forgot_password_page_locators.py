from selenium.webdriver.common.by import By


# локатор для кнопки перехода к странице восстановления пароля
OPEN_RESET_PASSWORD_PAGE_BUTTON_LOCATOR = [By.XPATH, ".//a[@href='/forgot-password']"]
# кнопка "Восстановить" / "Сохранить" на экране ввода емейла / пароля
RESET_BUTTON_LOCATOR = [By.XPATH, ".//button[contains(@class, 'button_type_primary')]"]
# поле для ввода емейла
MAIL_TEXT_FIELD_LOCATOR = [By.NAME, "name"]
# поле для ввода нового пароля
RESET_PASSWORD_FIELD_LOCATOR = [By.XPATH, ".//*[@type='password']"]
# Иконка глаза
EYE_ICON_LOCATOR = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]

# Подсветка поля для ввода пароля
PASSWORD_TEXT_FIELD_FOCUSED_LOCATOR = [By.XPATH, ".//label[contains(@class, 'input__placeholder-focused')]"]


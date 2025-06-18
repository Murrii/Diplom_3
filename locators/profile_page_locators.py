from selenium.webdriver.common.by import By


EXIT_BUTTON_LOCATOR = [By.XPATH, ".//button[contains(@class, 'Account_button')]"]
HISTORY_BUTTON_LOCATOR = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[contains(@href, '/account')]")
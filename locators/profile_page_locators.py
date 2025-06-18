from selenium.webdriver.common.by import By


EXIT_BUTTON_LOCATOR = [By.XPATH, ".//button[contains(@class, 'Account_button')]"]
HISTORY_BUTTON_LOCATOR = (By.XPATH, ".//a[contains(@href, '/account/order-history')]")
PERSONAL_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, ".//a[contains(@href, '/account')]")
ORDER_HISTORY_LIST_LOCATOR = (By.XPATH, ".//div[contains(@class, 'OrderHistory_orderHistory')]")

# Локатор активной вкладки
ACTIVE_TAB_LOCATOR = (By.XPATH, ".//li/a[@aria-current='page']")
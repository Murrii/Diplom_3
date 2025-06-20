from selenium.webdriver.common.by import By


FEED_BUTTON_LOCATOR = (By.XPATH, ".//a[@href='/feed']/p")
FEED_ORDERS_LOCATOR = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li")
FEED_ORDERS_IDS_LOCATOR = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li/a/div/p[contains(@class, 'text_type_digits-default')]")
MODAL_WINDOW_ORDER_INFO_LOCATOR = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")
ORDER_STATUS_FINISHED_TITLE_LOCATOR = (By.XPATH, ".//div[contains(@class, 'OrderFeed_orderStatusBox')]/p")
ORDER_COUNTERS_VALUES_LOCATOR = (By.XPATH, ".//p[contains(@class, 'OrderFeed_number')]")
ORDERS_IN_WORK_LIST_LOCATOR = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
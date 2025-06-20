from selenium.webdriver.common.by import By

CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, ".//p[text()='Конструктор']")

BUN_INGREDIENT_LOCATOR = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']/p")

MODAL_WINDOW_TITLE_LOCATOR = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//h2")

CLOSE_MODAL_WINDOW_BUTTON_LOCATOR = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'modal__close')]")

COUNTER_ICON_LOCATOR = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[contains(@class, 'counter_counter')]")

ORDER_SECTION_LOCATOR = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")

MAKE_ORDER_BUTTON_LOCATOR = (By.XPATH, ".//button[text()='Оформить заказ']")

ORDER_ID_LOCATOR = (By.XPATH, ".//div[contains(@class, 'contentBox')]/h2")
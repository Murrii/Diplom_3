from selenium.webdriver.common.by import By


EMAIL_INPUT = (By.XPATH, './/*[text()="Email"]/parent::div/input')  # поле для ввода емейла
PASS_INPUT = (By.NAME, 'Пароль')  # поле для ввода пароля
LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # Кнопка авторизации

# Для проверки успешной авторизации
GET_FOOD_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') # кнопка оформления заказа для авторизированного пользователя
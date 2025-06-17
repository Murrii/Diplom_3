from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ждем, пока элемент появится и возвращаем его
    def find_element_with_wait_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    # Ждем, пока элемент станет кликабельным и возвращаем его
    def find_element_with_wait_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    # Ждем, пока элемент станет кликабельным и нажимаем на него
    # Чтобы клик стабильно проходил в Firefox, при появлении перекрывающего окна кликаем по нижнему слою
    def click_on_element(self, locator):
        element = self.find_element_with_wait_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    # Получаем текст элемента и возвращаем его
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait_visibility(locator)
        return element.text

    # Заполняем поле текстом
    def fill_text_to_field(self, locator, text):
        self.find_element_with_wait_clickable(locator).send_keys(text)

    # Переходим по полученному url
    def go_to_url(self, url):
        self.driver.get(url)

    # Прокручиваем страницу до выбранного элемента и ждем пока все прогрузится
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element_with_wait_visibility(locator))
        self.find_element_with_wait_visibility(locator)

    # Прокручиваем страницу до конца
    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # Вводим данные в поле и подтверждаем ввод кнопкой ENTER
    def fill_the_field_and_click_enter(self, locator, text):
        element = self.find_element_with_wait_clickable(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
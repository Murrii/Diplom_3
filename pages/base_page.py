from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


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

    # drag-and-drop для chrome
    def drag_from_drop_to_chrome(self, locator_from, locator_to):
        element_from = self.find_element_with_wait_clickable(locator_from)
        element_to = self.find_element_with_wait_clickable(locator_to)
        action = ActionChains(self.driver)
        action.drag_and_drop(element_from, element_to).perform()

    # drag-and-drop для firefox
    def drag_from_drop_to_firefox(self, locator_from, locator_to):
        element_from = self.find_element_with_wait_clickable(locator_from)
        element_to = self.find_element_with_wait_clickable(locator_to)
        #action = ActionChains(self.driver)
        #action.click_and_hold(element_from).move_to_element(element_to).release().perform()
        self.driver.execute_script("""
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function (key, value) {
                            this.data[key] = value;
                        },
                        getData: function (key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                function dispatchEvent(element, event, transferData) {
                    if (transferData !== undefined) {
                        event.dataTransfer = transferData;
                    }
                    if (element.dispatchEvent) {
                        element.dispatchEvent(event);
                    } else if (element.fireEvent) {
                        element.fireEvent("on" + event.type, event);
                    }
                }

                var source = arguments[0];
                var target = arguments[1];
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(source, dragStartEvent);
                var dropEvent = createEvent('drop');
                dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
                var dragEndEvent = createEvent('dragend');
                dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
            """, element_from, element_to)

    # получаем текст элемента без указания локатора
    @staticmethod
    def get_text_from_element_without_locator(element):
        return element.text

    # Проверяем, что элемент не отображается на странице
    def is_element_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))
            return True
        except TimeoutError:
            return False

    # Проверяем, что элемент отображается на странице
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutError:
            return False

    # получаем список элементов
    def get_list_of_elements(self, locator):
        list_of_elements = self.driver.find_elements(*locator)
        return list_of_elements

    # ждем, пока изменится текст элемента
    def wait_change_of_element(self, locator, text_must_change):
        self.find_element_with_wait_visibility(locator)
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, str(text_must_change)))

    # ждем, пока в элементе появится текст
    def wait_text_is_visible(self, locator, text_must_visible):
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(locator, text_must_visible))
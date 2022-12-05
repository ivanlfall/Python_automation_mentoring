import inspect

from selenium.common import NoSuchElementException

from utilities.explicit_wait_context import ExplicitWait


class Element:

    def __init__(self, driver, locator, web_element=None, name=None):
        self.locator = locator
        self.driver = driver
        self.web_element = web_element
        self.name = name if name else self.__get_name_from_stack()

    def __get_element(self):
        if self.web_element:
            return self.web_element
        else:
            return self.driver.find_element(*self.locator)

    def click(self):
        self.__get_element().click()

    def insert_value(self, value):
        self.__get_element().clear()
        self.__get_element().send_keys(value)

    def is_present(self, wait_time=3):
        with ExplicitWait(self.driver, wait_time):
            try:
                self.__get_element()
                return True
            except NoSuchElementException:
                return False

    def get_inner_text(self):
        return self.__get_element().get_attribute('innerText')

    @staticmethod
    def list_from(driver, locator):
        web_elements = driver.find_elements(*locator)
        element_locator = lambda position: f"{locator}[{position}]"
        for position, web_element in enumerate(web_elements, start=1):
            yield Element(driver, element_locator(position), web_element=web_element)

    def __get_name_from_stack(self):
        for line in inspect.stack():
            if (parent := line[0].f_locals.get('self', None)) and isinstance(parent, self.__class__):
                continue
            return f"{parent.__class__.__name__}::{line.function}" if parent else line.function

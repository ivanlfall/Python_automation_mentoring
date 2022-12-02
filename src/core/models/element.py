import inspect

from selenium.common import NoSuchElementException

from utilities.explicit_wait_context import ExplicitWait


class Element:

    def __init__(self, driver, locator, element=None):
        self.locator = locator
        self.driver = driver
        self.element = element
        self.name = inspect.stack()[1].function  # Get function name that called to Element.__init__

    def __get_element(self):
        if self.element:
            return self.element
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

    def get_name(self):
        def formatted_name(name):
            return name.upper().replace("_", " ")

        return formatted_name(self.name)

    @staticmethod
    def list_from(driver, locator):
        elements = driver.find_elements(*locator)
        for element in elements:
            yield Element(driver, locator, element=element)


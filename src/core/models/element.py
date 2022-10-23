from selenium.common import NoSuchElementException

from utilities.utils import get_name_from_locator


class Element:

    def __init__(self, driver, locator, element=None):
        self.locator = locator
        self.driver = driver
        self.element = element

    def __get_element(self):
        if self.element is None:
            return self.driver.find_element(*self.locator)
        else:
            return self.element

    def click(self):
        self.__get_element().click()

    def insert_value(self, value):
        self.__get_element().clear()
        self.__get_element().send_keys(value)

    def is_present(self):
        try:
            self.__get_element()
            return True
        except NoSuchElementException:
            return False

    def get_inner_text(self):
        return self.__get_element().get_attribute('innerText')

    def get_content(self):
        return get_name_from_locator(self.locator[1])

    @staticmethod
    def list_from(driver, locator):
        elements = driver.find_elements(*locator)
        for element in elements:
            yield Element(driver, locator, element=element)


from selenium.common import NoSuchElementException

from utilities.utils import get_name_from_locator


class Element:

    def __init__(self, driver, locator):
        self.locator = locator
        self.driver = driver

    def __get_element(self):
        return self.driver.find_element(*self.locator)

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


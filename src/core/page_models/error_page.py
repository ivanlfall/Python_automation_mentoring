from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ErrorPage(BasePage):

    __ERROR_TITLE = (By.XPATH, '//h1')
    __ERROR_MESSAGE = (By.XPATH, '//pre[2]')

    def __init__(self, driver):
        self.driver = driver

    def error_title(self):
        return Element(self.driver, self.__ERROR_TITLE)

    def error_message(self):
        return Element(self.driver, self.__ERROR_MESSAGE)

    def elements(self):
        return [self.error_title(), self.error_message()]
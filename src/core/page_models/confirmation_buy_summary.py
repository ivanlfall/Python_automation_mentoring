from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ConfirmationBuySummary(BasePage):

    __CONFIRMATION_MESSAGE = (By.XPATH, '//ul//li')

    def __init__(self, driver):
        self.driver = driver

    def confirmation_message(self):
        return Element(self.driver, self.__CONFIRMATION_MESSAGE)
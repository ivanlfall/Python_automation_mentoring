from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class BuyDetails(BasePage):

    __CONTINUE_BUTTON = (By.CSS_SELECTOR, '[name=newOrder]')

    def __init__(self, driver):
        self.driver = driver

    def continue_button(self):
        return Element(self.driver, self.__CONTINUE_BUTTON)
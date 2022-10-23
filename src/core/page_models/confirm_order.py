from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ConfirmOrder(BasePage):

    __CONFIRM_BUTTON = (By.CSS_SELECTOR, '[class=Button]')

    def __init__(self, driver):
        self.driver = driver

    def confirm_button(self):
        return Element(self.driver, self.__CONFIRM_BUTTON)
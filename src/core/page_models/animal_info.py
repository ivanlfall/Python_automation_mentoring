from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class AnimalInfo(BasePage):

    __ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "[class='Button']")

    def __init__(self, driver):
        self.driver = driver

    def add_to_card_button(self):
        return Element(self.driver, self.__ADD_TO_CARD_BUTTON)
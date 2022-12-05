import random

from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class SpecificBreedCatalog(BasePage):

    __ITEM_BUTTONS = (By.XPATH, '(//td/a[not(@class="Button")])')

    def __init__(self, driver):
        self.driver = driver

    def pet_item(self):
        elements = list(Element.list_from(self.driver, self.__ITEM_BUTTONS))
        return random.choice(elements)
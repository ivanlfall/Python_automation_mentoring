import random

from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class SpecificDogCatalog(BasePage):

    __DOG_ITEM_BUTTONS = (By.CSS_SELECTOR, 'td>a:not([class=Button])')

    def __init__(self, driver):
        self.driver = driver

    def dog_item(self):
        elements = list(Element.list_from(self.driver, self.__DOG_ITEM_BUTTONS))
        return random.choice(elements)
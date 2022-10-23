import random

from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class DogCatalog(BasePage):

    __DOG_BREED_BUTTONS = (By.CSS_SELECTOR, "td>a")

    def __init__(self, driver):
        self.driver = driver

    def dog_breed_choice(self):
        elements = list(Element.list_from(self.driver, self.__DOG_BREED_BUTTONS))
        return random.choice(elements)


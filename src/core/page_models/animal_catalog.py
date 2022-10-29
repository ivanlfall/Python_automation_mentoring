from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class AnimalCatalog(BasePage):

    __ANIMAL_BREED_BUTTONS = (By.XPATH, '//td[contains(text(),"{}")]/preceding-sibling::td/a')

    def __init__(self, driver):
        self.driver = driver

    def animal_breed_choice(self, breed):
        by, selector = self.__ANIMAL_BREED_BUTTONS
        selector = selector.format(breed.capitalize())
        return Element(self.driver, (by, selector))

from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class DogCatalog(BasePage):

    A_DOG = (By.XPATH, "//a[text()='K9-BD-01']")

    def __init__(self, driver):
        self.driver = driver

    def choose_a_dog_button(self):
        return Element(self.driver, self.A_DOG)


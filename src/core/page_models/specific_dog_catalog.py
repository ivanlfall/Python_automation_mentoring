from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class SpecificDogCatalog(BasePage):

    DOG_ITEM = (By.XPATH, "//a[text()='EST-6']")

    def __init__(self, driver):
        self.driver = driver

    def dog_item(self):
        return Element(self.driver, self.DOG_ITEM)
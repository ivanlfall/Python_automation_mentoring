from selenium.webdriver.common.by import By

from core.models.element import Element
from urls import HOME_PET_STORE
from core.page_models.base_page import BasePage


class IndexPetStore(BasePage):

    SIGN_IN = (By.XPATH, '//a[contains(text(),"Sign In")]')
    SEARCH_BUTTON = (By.NAME, 'searchProducts')
    SEARCH_INPUT = (By.NAME, 'keyword')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(HOME_PET_STORE)

    def title(self):
        return self.driver.title

    def sign_in_button(self):
        return Element(self.driver, self.SIGN_IN)

    def search_input(self):
        return Element(self.driver, self.SEARCH_INPUT)

    def search_button(self):
        return Element(self.driver, self.SEARCH_BUTTON)
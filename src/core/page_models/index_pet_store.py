from selenium.webdriver.common.by import By

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

    def search_pet(self, search_input):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(search_input)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def title(self):
        return self.driver.title

    def go_to_sign_in(self):
        self.driver.find_element(*self.SIGN_IN).click()

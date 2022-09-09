from selenium.webdriver.common.by import By

from config import HOME_PET_STORE


class IndexPetStore:

    SIGN_IN = (By.XPATH, '//a[contains(text(),"Sign In")]')
    SEARCH_BUTTON = (By.NAME, 'searchProducts')
    SEARCH_INPUT = (By.NAME, 'keyword')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(HOME_PET_STORE)

    def search_pet(self, search_input):
        pass
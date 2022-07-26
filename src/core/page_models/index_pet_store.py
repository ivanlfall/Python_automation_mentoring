from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage
from resources.urls import HOME_PET_STORE


class IndexPetStore(BasePage):

    __SIGN_IN = (By.XPATH, '//a[contains(text(),"Sign In")]')
    __SEARCH_BUTTON = (By.NAME, 'searchProducts')
    __SEARCH_INPUT = (By.NAME, 'keyword')
    __SIDE_BAR = (By.CSS_SELECTOR, '[id=SidebarContent]')
    __MAIN_CONTENT = (By.CSS_SELECTOR, '[id=MainImageContent]')
    __SIDE_BAR_DOGS_BUTTON = (By.XPATH, "//*[@id='SidebarContent']//a[contains(@href, 'DOGS')]")
    __SIDE_BAR_CATS_BUTTON = (By.XPATH, "//*[@id='SidebarContent']//a[contains(@href, 'CATS')]")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(HOME_PET_STORE)

    def title(self):
        return self.driver.title

    def sign_in_button(self):
        return Element(self.driver, self.__SIGN_IN)

    def search_input(self):
        return Element(self.driver, self.__SEARCH_INPUT)

    def search_button(self):
        return Element(self.driver, self.__SEARCH_BUTTON)

    def side_bar_dogs_button(self):
        return Element(self.driver, self.__SIDE_BAR_DOGS_BUTTON)

    def side_bar_cats_button(self):
        return Element(self.driver, self.__SIDE_BAR_CATS_BUTTON)

    def side_bar(self):
        return Element(self.driver, self.__SIDE_BAR)

    def main_content(self):
        return Element(self.driver, self.__MAIN_CONTENT)

    def elements(self):
        return [self.sign_in_button(), self.side_bar(), self.main_content()]

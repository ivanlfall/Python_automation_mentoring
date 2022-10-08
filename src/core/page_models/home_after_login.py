from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class HomeAfterLogin(BasePage):

    SIGN_OUT = (By.XPATH, '//a[contains(text(),"Sign Out")]')
    SIDE_BAR = (By.CSS_SELECTOR, '[id=SidebarContent]')
    MAIN_CONTENT = (By.CSS_SELECTOR, '[id=MainImageContent]')
    WELCOME_MESSAGE = (By.CSS_SELECTOR, '[id=WelcomeContent]')
    MY_ACCOUNT_BUTTON = (By.XPATH, '//a[contains(text(),"My Account")]')

    def __init__(self, driver):
        self.driver = driver

    def sign_out_button(self):
        return Element(self.driver, self.SIGN_OUT)

    def welcome_message(self):
        return Element(self.driver, self.WELCOME_MESSAGE)

    def my_account_button(self):
        return Element(self.driver, self.MY_ACCOUNT_BUTTON)

    def elements(self):
        return [self.welcome_message(), self.my_account_button(), self.sign_out_button()]
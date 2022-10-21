from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage
from urls import SIGN_IN


class SignInPetStore(BasePage):

    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Register")]')
    USERNAME_INPUT = (By.CSS_SELECTOR, "[name=username]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name=password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=signon]")
    MESSAGES_BLOCK = (By.CSS_SELECTOR, "[class=messages]")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(SIGN_IN)

    def register_button(self):
        return Element(self.driver, self.REGISTER_BUTTON)

    def username_input(self):
        return Element(self.driver, self.USERNAME_INPUT)

    def password_input(self):
        return Element(self.driver, self.PASSWORD_INPUT)

    def login_button(self):
        return Element(self.driver, self.LOGIN_BUTTON)

    def message_block(self):
        return Element(self.driver, self.MESSAGES_BLOCK)

    def elements(self):
        return [self.register_button(), self.username_input(), self.password_input()]
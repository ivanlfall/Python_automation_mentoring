from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage
from resources.data import INDEX_TITLE
from urls import REGISTER_USER_PAGE


class RegisterPage(BasePage):

    USER_ID = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "[name='repeatedPassword']")
    FIRST_NAME = (By.CSS_SELECTOR, "[name='account.firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[name='account.lastName']")
    EMAIL = (By.CSS_SELECTOR, "[name='account.email']")
    PHONE = (By.CSS_SELECTOR, "[name='account.phone']")
    ADDRESS = (By.CSS_SELECTOR, "[name='account.address1']")
    CITY = (By.CSS_SELECTOR, "[name='account.city']")
    STATE = (By.CSS_SELECTOR, "[name='account.state']")
    ZIP = (By.CSS_SELECTOR, "[name='account.zip']")
    COUNTRY = (By.CSS_SELECTOR, "[name='account.country']")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "[name='newAccount']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(REGISTER_USER_PAGE)

    def was_user_registered(self):
        return self.driver.title == INDEX_TITLE

    def username_input(self):
        return Element(self.driver, self.USER_ID)

    def password_input(self):
        return Element(self.driver, self.PASSWORD)

    def repeat_password_input(self):
        return Element(self.driver, self.REPEAT_PASSWORD)

    def first_name_input(self):
        return Element(self.driver, self.FIRST_NAME)

    def last_name_input(self):
        return Element(self.driver, self.LAST_NAME)

    def email_input(self):
        return Element(self.driver, self.EMAIL)

    def phone_input(self):
        return Element(self.driver, self.PHONE)

    def address_input(self):
        return Element(self.driver, self.ADDRESS)

    def city_input(self):
        return Element(self.driver, self.CITY)

    def state_input(self):
        return Element(self.driver, self.STATE)

    def zip_code_input(self):
        return Element(self.driver, self.ZIP)

    def country_input(self):
        return Element(self.driver, self.COUNTRY)

    def create_account_button(self):
        return Element(self.driver, self.CREATE_ACCOUNT)





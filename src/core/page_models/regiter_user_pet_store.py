from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage
from resources.data import INDEX_TITLE
from urls import REGISTER_USER_PAGE


class RegisterPage(BasePage):

    __USER_ID = (By.CSS_SELECTOR, "[name='username']")
    __PASSWORD = (By.CSS_SELECTOR, "[name='password']")
    __REPEAT_PASSWORD = (By.CSS_SELECTOR, "[name='repeatedPassword']")
    __FIRST_NAME = (By.CSS_SELECTOR, "[name='account.firstName']")
    __LAST_NAME = (By.CSS_SELECTOR, "[name='account.lastName']")
    __EMAIL = (By.CSS_SELECTOR, "[name='account.email']")
    __PHONE = (By.CSS_SELECTOR, "[name='account.phone']")
    __ADDRESS = (By.CSS_SELECTOR, "[name='account.address1']")
    __CITY = (By.CSS_SELECTOR, "[name='account.city']")
    __STATE = (By.CSS_SELECTOR, "[name='account.state']")
    __ZIP = (By.CSS_SELECTOR, "[name='account.zip']")
    __COUNTRY = (By.CSS_SELECTOR, "[name='account.country']")
    __CREATE_ACCOUNT = (By.CSS_SELECTOR, "[name='newAccount']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(REGISTER_USER_PAGE)

    def was_user_registered(self):
        return self.driver.title == INDEX_TITLE

    def username_input(self):
        return Element(self.driver, self.__USER_ID)

    def password_input(self):
        return Element(self.driver, self.__PASSWORD)

    def repeat_password_input(self):
        return Element(self.driver, self.__REPEAT_PASSWORD)

    def first_name_input(self):
        return Element(self.driver, self.__FIRST_NAME)

    def last_name_input(self):
        return Element(self.driver, self.__LAST_NAME)

    def email_input(self):
        return Element(self.driver, self.__EMAIL)

    def phone_input(self):
        return Element(self.driver, self.__PHONE)

    def address_input(self):
        return Element(self.driver, self.__ADDRESS)

    def city_input(self):
        return Element(self.driver, self.__CITY)

    def state_input(self):
        return Element(self.driver, self.__STATE)

    def zip_code_input(self):
        return Element(self.driver, self.__ZIP)

    def country_input(self):
        return Element(self.driver, self.__COUNTRY)

    def create_account_button(self):
        return Element(self.driver, self.__CREATE_ACCOUNT)





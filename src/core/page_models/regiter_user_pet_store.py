from selenium.webdriver.common.by import By

from core.page_models.base_page import BasePage
from resources.data import INDEX_TITLE


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

    def was_user_registered(self):
        return self.driver.title == INDEX_TITLE

    def create_account(self, user):
        self.driver.find_element(*self.USER_ID).send_keys(user.id)
        self.driver.find_element(*self.PASSWORD).send_keys(user.password)
        self.driver.find_element(*self.REPEAT_PASSWORD).send_keys(user.password)
        self.driver.find_element(*self.FIRST_NAME).send_keys(user.first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(user.last_name)
        self.driver.find_element(*self.EMAIL).send_keys(user.email)
        self.driver.find_element(*self.PHONE).send_keys(user.phone)
        self.driver.find_element(*self.ADDRESS).send_keys(user.address)
        self.driver.find_element(*self.CITY).send_keys(user.city)
        self.driver.find_element(*self.STATE).send_keys(user.state)
        self.driver.find_element(*self.ZIP).send_keys(user.zip_code)
        self.driver.find_element(*self.COUNTRY).send_keys(user.country)
        self.driver.find_element(*self.CREATE_ACCOUNT).click()


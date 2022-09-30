from selenium.webdriver.common.by import By

from core.page_models.base_page import BasePage


class SignInPetStore(BasePage):

    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Register")]')
    USERNAME_INPUT = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='signon']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_register_page(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

    def login_user(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

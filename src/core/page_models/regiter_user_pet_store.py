from selenium.webdriver.common.by import By


class RegisterPage:

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

    def go_to_register_page(self):
        pass


    def create_account(self, user_id, password, repeat_password, first_name, last_name, email,
                       phone, address, city, state, zip_code, country):
        self.driver.find_element(*self.USER_ID).send_keys(user_id)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.REPEAT_PASSWORD).send_keys(repeat_password)
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.COUNTRY).send_keys(country)
        self.driver.find_element(*self.CREATE_ACCOUNT).click()


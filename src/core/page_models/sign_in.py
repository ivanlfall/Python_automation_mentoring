from selenium.webdriver.common.by import By


class SignInPetStore:

    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Register")]')

    def __init__(self, driver):
        self.driver = driver

    def go_to_register_page(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()

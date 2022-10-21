from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ShoppingCart(BasePage):

    PROCEED_TO_CHECKOUT = (By.XPATH, '//a[contains(text(),"Proceed to Checkout")]')

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        return Element(self.driver, self.PROCEED_TO_CHECKOUT)
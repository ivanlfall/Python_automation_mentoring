from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ResultPagePetStore(BasePage):

    __RESULT_LINKS = (By.XPATH, '(//div/table/tbody/tr/td)')

    def __init__(self, driver):
        self.driver = driver

    def result_links(self):
        elements = Element.list_from(self.driver, self.__RESULT_LINKS)
        return elements


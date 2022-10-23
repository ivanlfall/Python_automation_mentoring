from selenium.webdriver.common.by import By

from core.models.element import Element
from core.page_models.base_page import BasePage


class ResultPagePetStore(BasePage):

    __RESULT_LINKS = (By.XPATH, '//div/table/tbody/tr/td')

    def __init__(self, driver):
        self.driver = driver

    def get_result_list(self):
        links = self.driver.find_elements(*self.__RESULT_LINKS)
        return [title.text for title in links]

    def get_actual_result(self):
        return Element(self.driver, self.__RESULT_LINKS)


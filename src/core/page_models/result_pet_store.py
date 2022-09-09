from selenium.webdriver.common.by import By


class ResultPagePetStore:

    RESULT_LINKS = (By.XPATH, '//div/table/tbody/tr/td')

    def __init__(self, browser):
        self.browser = browser

    def get_result_list(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        return [title.text for title in links]



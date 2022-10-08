
class Element:

    def __init__(self, driver, locator):
        self.element = driver.find_element(*locator)

    def click(self):
        self.element.click()

    def insert_value(self, value):
        self.element.clear()
        self.element.send_keys(value)

    def is_present(self):
        return self.element.is_displayed()

    def get_inner_text(self):
        return self.element.get_attribute('innerText')

    def get_content(self):
        return self.element



class Element:

    def __init__(self, driver, locator):
        self.element = driver.find_element(*locator)

    def click(self):
        self.element.click()

    def insert_value(self, value):
        self.element.send_keys(value)

    def is_present(self):
        self.element.is_present()
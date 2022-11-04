import random
import string


def get_name_from_locator(locator):
    if '"' in locator:
        start = locator.find('"') + 1
        end = locator.rfind('"')
        return locator[start:end]
    elif '=' in locator:
        start = locator.find('=') + 1
        end = locator.find(']')
        return locator[start:end]
    else:
        return locator


def get_random_text():
    number_of_char = 10
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=number_of_char))


class ExplicitWait:

    def __init__(self, driver, seconds):
        self.driver = driver
        self.seconds = seconds
        self.default_seconds = driver.timeouts.implicit_wait

    def __enter__(self):
        self.driver.implicitly_wait(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.implicitly_wait(self.default_seconds)


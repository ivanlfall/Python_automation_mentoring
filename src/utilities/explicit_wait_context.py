"""
To use as a context in a with statement. During the context life the implicit wait will change to x seconds
passed as parameter.
This context allow you to manage the wait time by demand.
"""


class ExplicitWait:

    def __init__(self, driver, seconds):
        self.driver = driver
        self.seconds = seconds
        self.default_seconds = driver.timeouts.implicit_wait

    def __enter__(self):
        self.driver.implicitly_wait(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.implicitly_wait(self.default_seconds)
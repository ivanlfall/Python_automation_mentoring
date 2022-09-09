import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    b = webdriver.Chrome(service=service, options=options)
    b.implicitly_wait(10)
    yield b
    b.quit()
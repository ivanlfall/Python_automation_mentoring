import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from core.page_models.home_after_login import HomeAfterLogin
from core.page_models.index_pet_store import IndexPetStore
from core.page_models.regiter_user_pet_store import RegisterPage
from core.page_models.result_pet_store import ResultPagePetStore
from core.page_models.sign_in import SignInPetStore


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def index_home(driver):
    yield IndexPetStore(driver)


@pytest.fixture
def register_page(driver):
    yield RegisterPage(driver)


@pytest.fixture
def sign_in_page(driver):
    yield SignInPetStore(driver)


@pytest.fixture
def result_page(driver):
    yield ResultPagePetStore(driver)


@pytest.fixture
def home_after_login(driver):
    yield HomeAfterLogin(driver)
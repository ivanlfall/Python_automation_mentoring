import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from core.page_models.animal_catalog import AnimalCatalog
from core.page_models.animal_info import AnimalInfo
from core.page_models.buy_details import BuyDetails
from core.page_models.confirm_order import ConfirmOrder
from core.page_models.confirmation_buy_summary import ConfirmationBuySummary
from core.page_models.error_page import ErrorPage
from core.page_models.home_after_login import HomeAfterLogin
from core.page_models.index_pet_store import IndexPetStore
from core.page_models.regiter_user_pet_store import RegisterPage
from core.page_models.result_pet_store import ResultPagePetStore
from core.page_models.shopping_cart import ShoppingCart
from core.page_models.sign_in import SignInPetStore
from core.page_models.specific_breed_catalog import SpecificBreedCatalog


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


@pytest.fixture
def animal_catalog(driver):
    yield AnimalCatalog(driver)


@pytest.fixture
def specific_breed_catalog(driver):
    yield SpecificBreedCatalog(driver)


@pytest.fixture
def animal_info(driver):
    yield AnimalInfo(driver)


@pytest.fixture
def shopping_cart(driver):
    yield ShoppingCart(driver)


@pytest.fixture
def buy_details(driver):
    yield BuyDetails(driver)


@pytest.fixture
def confirm_order(driver):
    yield ConfirmOrder(driver)


@pytest.fixture
def confirmation_buy_summary(driver):
    yield ConfirmationBuySummary(driver)


@pytest.fixture
def error_page(driver):
    yield ErrorPage(driver)
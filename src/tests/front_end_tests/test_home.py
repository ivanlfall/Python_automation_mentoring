import pytest
from assertpy import assert_that

from core.page_models.index_pet_store import IndexPetStore
from core.page_models.result_pet_store import ResultPagePetStore



def test_home(driver):
    index_home = IndexPetStore(driver)
    index_home.load()
    assert_that(index_home.title()).is_equal_to('JPetStore Demo')


def test_search_bar(driver):
    index_home = IndexPetStore(driver)
    result_page = ResultPagePetStore(driver)
    search_input = 'Bulldog'
    index_home.load()
    index_home.search_pet(search_input)
    search_result = result_page.get_result_list()
    assert_that(search_result).contains(search_input)

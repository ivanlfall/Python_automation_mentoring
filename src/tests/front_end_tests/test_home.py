from assertpy import assert_that


def test_home(index_home):
    index_home.load()
    assert_that(index_home.title()).is_equal_to('JPetStore Demo')


def test_search_bar(index_home, result_page):
    search_input = 'Bulldog'
    index_home.load()
    index_home.search_pet(search_input)
    search_result = result_page.get_result_list()
    assert_that(search_result).contains(search_input)

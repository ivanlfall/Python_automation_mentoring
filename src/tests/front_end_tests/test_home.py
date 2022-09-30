from assertpy import assert_that

from resources.data import INDEX_TITLE
from utils.get_me import Factory


def test_home(index_home):
    index_home.load()
    assert_that(index_home.title()).is_equal_to(INDEX_TITLE)


def test_search_bar(index_home, result_page):
    search_input = 'Bulldog'
    index_home.load()
    index_home.search_pet(search_input)
    search_result = result_page.get_result_list()
    assert_that(search_result).contains(search_input)


def test_register_user(index_home, sign_in_page, register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    index_home.load()
    index_home.go_to_sign_in()
    sign_in_page.go_to_register_page()
    register_page.create_account(user)
    assert_that(register_page.was_user_registered()).is_equal_to(True)

def test_login(index_home, sign_in_page, register_page):
    username, password = create_account(index_home, sign_in_page, register_page)
    sign_in_page.login_user(username, password)


def create_account(index_home, sign_in_page, register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    index_home.load()
    index_home.go_to_sign_in()
    sign_in_page.go_to_register_page()
    register_page.create_account(user)
    return user['user_id'], user['password']

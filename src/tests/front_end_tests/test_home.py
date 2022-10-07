from assertpy import assert_that

from resources.data import INDEX_TITLE
from utils.get_me import Factory


def test_home(index_home):
    index_home.load()
    assert_that(index_home.title()).is_equal_to(INDEX_TITLE)


def test_search_bar(index_home, result_page):
    search_input = 'Bulldog'
    index_home.load()
    index_home.search_input().insert_value(search_input)
    index_home.search_button().click()
    search_result = result_page.get_result_list()
    assert_that(search_result).contains(search_input)


def test_register_user(index_home, sign_in_page, register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    index_home.load()
    index_home.sign_in_button().click()
    sign_in_page.register_button().click()
    register_page.create_account(user)
    assert_that(register_page.was_user_registered()).is_equal_to(True)

def test_login(index_home, sign_in_page, register_page):
    username, password = create_account(index_home, sign_in_page, register_page)
    index_home.sign_in_button().click()
    sign_in_page.username_input().insert_value(username)
    sign_in_page.password_input().insert_value(password)
    sign_in_page.login_button().click()


def create_account(index_home, sign_in_page, register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    index_home.load()
    index_home.sign_in_button().click()
    sign_in_page.register_button().click()
    register_page.create_account(user)
    return user.id, user.password

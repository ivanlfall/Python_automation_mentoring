from assertpy import assert_that

from resources.data import INDEX_TITLE
from utils.get_me import Factory
from utils.print_with_format import print_sent_payload_from_object


def test_home(index_home):
    index_home.load()
    assert_that(index_home.title()).is_equal_to(INDEX_TITLE)
    assert_page_elements(index_home.elements())


def test_search_bar(index_home, result_page):
    search_input = 'Bulldog'
    index_home.load()
    index_home.search_input().insert_value(search_input)
    index_home.search_button().click()
    content_result = result_page.get_result_list()
    assert_that(content_result).contains(search_input)


def test_register_user(index_home, sign_in_page, register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    index_home.load()
    index_home.sign_in_button().click()
    sign_in_page.register_button().click()

    register_page.username_input().insert_value(user.id)
    register_page.password_input().insert_value(user.password)
    register_page.repeat_password_input().insert_value(user.password)
    register_page.first_name_input().insert_value(user.first_name)
    register_page.last_name_input().insert_value(user.last_name)
    register_page.email_input().insert_value(user.email)
    register_page.phone_input().insert_value(user.phone)
    register_page.address_input().insert_value(user.address)
    register_page.city_input().insert_value(user.city)
    register_page.state_input().insert_value(user.state)
    register_page.zip_code_input().insert_value(user.zip_code)
    register_page.country_input().insert_value(user.country)
    register_page.create_account_button().click()
    print_sent_payload_from_object(user)

    assert_page_elements(index_home.elements())


def test_login(index_home, sign_in_page, register_page, home_after_login):
    username, password = create_account(register_page)
    index_home.sign_in_button().click()
    sign_in_page.username_input().insert_value(username)
    sign_in_page.password_input().insert_value(password)
    sign_in_page.login_button().click()

    assert_page_elements(home_after_login.elements())


def create_account(register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    register_page.load()
    register_page.username_input().insert_value(user.id)
    register_page.password_input().insert_value(user.password)
    register_page.repeat_password_input().insert_value(user.password)
    register_page.first_name_input().insert_value(user.first_name)
    register_page.last_name_input().insert_value(user.last_name)
    register_page.email_input().insert_value(user.email)
    register_page.phone_input().insert_value(user.phone)
    register_page.address_input().insert_value(user.address)
    register_page.city_input().insert_value(user.city)
    register_page.state_input().insert_value(user.state)
    register_page.zip_code_input().insert_value(user.zip_code)
    register_page.country_input().insert_value(user.country)
    register_page.create_account_button().click()
    print_sent_payload_from_object(user)

    return user.id, user.password


def assert_page_elements(elements):
    for element in elements:
        assert_that(element.is_present()).described_as(element.get_content()).is_true()
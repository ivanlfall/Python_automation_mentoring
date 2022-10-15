import requests
from assertpy import assert_that

from core.api_wrappers.user_client import UserClient
from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema, \
    assert_successful_operation
from core.models.response_user import ResponseUser
from utilities.get_me import Factory
from utilities.print_with_format import print_test_info, print_test_info_with_schema

_factory = Factory()
_user = UserClient()
schema = {
    "id": {'type': 'number'},
    "username": {'type': 'string'},
    "firstName": {'type': 'string'},
    "lastName": {'type': 'string'},
    "email": {'type': 'string'},
    "password": {'type': 'string'},
    "phone": {'type': 'string'},
    "userStatus": {'type': 'number'}
}


# ----------------------- users - sign in -----------------------
def test_existing_user_can_login():
    user, _ = _user.create_user()
    login_response = _user.login_user(user.username, user.password)
    print_test_info(login_response.endpoint, user.__dict__, login_response.as_dict, login_response.status_code)

    assert_successful_operation(login_response)
    assert_that(login_response.as_dict['message']).contains('logged in user session:')


def test_non_existing_user_cant_login():
    fake_user = _factory.get_me(Factory.USER)
    login_response = _user.login_user(fake_user.username, fake_user.password)
    print_test_info(login_response.endpoint, fake_user.__dict__, login_response.as_dict, login_response.status_code)

    assert_that(login_response.status_code).described_as("Status code").is_equal_to(requests.codes.bad_request)
    assert_that(login_response.as_dict['message']).contains('Invalid username/password supplied')


def test_cant_login_with_username_empty():
    fake_user = _factory.get_me(Factory.USER)
    login_data = {'username': '', 'password': fake_user.password}
    login_response = _user.login_user(login_data['username'], login_data['password'])
    print_test_info(login_response.endpoint, login_data, login_response.as_dict, login_response.status_code)

    assert_that(login_response.status_code).described_as("Status code").is_equal_to(requests.codes.bad_request)
    assert_that(login_response.as_dict['message']).contains('Invalid username/password supplied')


# ----------------------- Extra tests -----------------------
def test_get_user_by_username():
    body = _factory.get_me(Factory.USER)
    created_user, _ = _user.create_user(body)

    response = _user.get_user_by_username(created_user.username)
    user = ResponseUser(
        response.status_code,
        response.text,
        response.as_dict['id'],
        created_user.first_name,
        created_user.last_name
    )

    assert_that(user.get_user().get('id')).is_equal_to(created_user.id)


# ----------------------- Extra tests -----------------------
def test_new_user_can_be_added():
    user = _factory.get_me(Factory.USER)
    _, response = _user.create_user(user)
    response_user = _user.get_user_by_username(user.username).as_dict

    print_test_info(response.endpoint, user.__dict__, response_user, response.status_code)

    assert_successful_operation(response)
    assert_that_body_content_are_equals(user.__dict__, response_user)


def test_created_user_can_be_deleted():
    user, _ = _user.create_user()

    response = _user.delete_user_by_username(user.username)
    assert_successful_operation(response)

    check_user = _user.get_user_by_username(user.username)
    print_test_info(response.endpoint, user.__dict__, response.as_dict, response.status_code)
    assert_that(check_user.status_code).is_equal_to(requests.codes.not_found)


def test_read_one_user_operation_has_expected_schema():
    user, _ = _user.create_user()
    got_user = _user.get_user_by_username(user.username)

    print_test_info_with_schema(got_user.endpoint, got_user.as_dict, schema)

    assert_that_is_the_correct_schema(schema, got_user.as_dict)
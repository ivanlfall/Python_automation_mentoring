import requests
from assertpy import assert_that

from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema
from core.models.user import User
from core.models_api.user_client import UserClient
from utils.helpers.get_me import Factory
from utils.helpers.print_with_format import print_test_info, print_test_info_with_schema

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
    login_response = _user.login_user(user['username'], user['password'])
    print_test_info(login_response.endpoint, user, login_response.as_dict, login_response.status_code)

    assert_that(login_response.status_code).is_equal_to(requests.codes.ok)
    assert_that(login_response.as_dict['message']).contains('logged in user session:')


def test_non_existing_user_cant_login():
    fake_user = _factory.get_me(Factory.USER)
    login_response = _user.login_user(fake_user['username'], fake_user['password'])
    print_test_info(login_response.endpoint, fake_user, login_response.as_dict, login_response.status_code)

    assert_that(login_response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(login_response.as_dict['message']).contains('Invalid username/password supplied')


def test_cant_login_with_username_empty():
    fake_user = _factory.get_me(Factory.USER)
    login_data = {'username': '', 'password': fake_user['password']}
    login_response = _user.login_user(login_data['username'], login_data['password'])
    print_test_info(login_response.endpoint, login_data, login_response.as_dict, login_response.status_code)

    assert_that(login_response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(login_response.as_dict['message']).contains('Invalid username/password supplied')


# ----------------------- Extra tests -----------------------
def test_get_user_by_username():
    body = _factory.get_me(Factory.USER)
    created_user, _ = _user.create_user(body)

    response = _user.get_user_by_username(created_user['username'])
    user = User(
        response.status_code,
        response.text,
        response.as_dict['id'],
        created_user['first_name'],
        created_user['last_name']
    )

    assert_that(user.get_user().get('id')).is_equal_to(created_user['id'])


# ----------------------- Extra tests -----------------------
def test_new_user_can_be_added():
    body = _factory.get_me(Factory.USER)
    _, response = _user.create_user(body)
    response_user = _user.get_user_by_username(body['username']).as_dict

    print_test_info(response.endpoint, body, response_user, response.status_code)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that_body_content_are_equals(body, response_user)


def test_created_user_can_be_deleted():
    user, response = _user.create_user()

    response = _user.delete_user_by_username(user['username'])
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    check_user = _user.get_user_by_username(user['username'])
    print_test_info(response.endpoint, user, response.as_dict, response.status_code)
    assert_that(check_user.status_code).is_equal_to(requests.codes.not_found)


def test_read_one_user_operation_has_expected_schema():
    body = _factory.get_me(Factory.USER)
    _user.create_user(body)
    user = _user.get_user_by_username(body['username'])

    print_test_info_with_schema(user.endpoint, user.as_dict, schema)

    assert_that_is_the_correct_schema(schema, user.as_dict)
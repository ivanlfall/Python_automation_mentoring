import requests
from assertpy import assert_that

from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema
from utils.helpers.get_me import Factory
from utils.helpers.print_with_format import print_test_info, print_test_info_with_schema
from utils.user_client import UserClient

_factory = None
user_client = None
schema = None


def setup():
    global _factory, user_client, schema
    print('\n########### SETUP ###########')
    _factory = Factory()
    user_client = UserClient()
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


def test_new_user_can_be_added():
    body = _factory.get_me(Factory.USER)
    _, response = user_client.create_user(body)
    response_user = user_client.get_user_by_username(body['username']).as_dict

    print_test_info(body, response_user, response.status_code)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that_body_content_are_equals(body, response_user)


def test_created_user_can_be_deleted():
    user, response = user_client.create_user()

    response = user_client.delete_user_by_username(user['username'])
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    check_user = user_client.get_user_by_username(user['username'])
    print_test_info(user, response.as_dict, response.status_code)
    assert_that(check_user.status_code).is_equal_to(requests.codes.not_found)


def test_read_one_user_operation_has_expected_schema():
    body = _factory.get_me(Factory.USER)
    user_client.create_user(body)
    user = user_client.get_user_by_username(body['username'])

    print_test_info_with_schema(user.as_dict, schema)

    assert_that_is_the_correct_schema(schema, user.as_dict)

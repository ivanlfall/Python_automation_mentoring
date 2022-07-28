import json

import requests
from assertpy import assert_that

from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema

from utils.helpers.get_me import Factory
from utils.user_client import UserClient

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

_factory = Factory()
user_client = UserClient()


def test_new_user_can_be_added():

    user_name, body = _factory.get_me(Factory.USER)
    _, response = user_client.create_user(body)

    response_user = user_client.get_user_by_username(user_name).as_dict

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that_body_content_are_equals(body, response_user)


def test_created_user_can_be_deleted():

    user_name, body = _factory.get_me(Factory.USER)
    user_client.create_user(body)

    response = user_client.delete_user_by_username(user_name)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    check_user = user_client.get_user_by_username(user_name)
    assert_that(check_user.status_code).is_equal_to(requests.codes.not_found)


def test_read_one_user_operation_has_expected_schema():
    user_name, body = _factory.get_me(Factory.USER)
    user_client.create_user(body)

    response = user_client.get_user_by_username(user_name)
    user = json.loads(response.text)

    assert_that_is_the_correct_schema(schema, user)
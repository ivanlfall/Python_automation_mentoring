import json

import requests
from assertpy import assert_that

from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema
from utils.helpers.get_me import Factory
from utils.pet_client import PetClient

schema = {
    "id": {'type': 'number'},
    "category": {'type': 'dict'},
    "name": {'type': 'string'},
    "photoUrls": {'type': 'list'},
    "tags": {'type': 'list'},
    "status": {'type': 'string'}
}
_factory = Factory()
pet_client = PetClient()


def test_new_pet_can_be_added():

    pet_id, body = _factory.get_me(Factory.PET)
    _, response = pet_client.create_pet(body)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that_body_content_are_equals(body, response.as_dict)


def test_created_pet_can_be_deleted():
    pet_id, _ = pet_client.create_pet()

    response = pet_client.delete_pet_by_id(pet_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_read_one_operation_has_expected_schema():
    pet_id, _ = pet_client.create_pet()
    response = pet_client.get_pet_by_id(pet_id)
    pet = json.loads(response.text)
    # pet['name'] = 22


    assert_that_is_the_correct_schema(schema, pet)
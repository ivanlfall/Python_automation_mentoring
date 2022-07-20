import json

from cerberus import Validator
import requests
from assertpy import assert_that

from utils.helpers.get_me import Factory
from utils.pet_client import PetClient

from core.assertions.custom_assertions import assert_that_body_content_are_equals

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
    response = pet_client.get_pet_by_id(123)
    pet = json.loads(response.text)

    validator = Validator(schema)
    is_valid = validator.validate(pet)

    assert_that(is_valid, description=validator.errors).is_true()
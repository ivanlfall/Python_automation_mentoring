import json

from cerberus import Validator
import requests
from assertpy import assert_that

from utils.pet_client import PetClient


schema = {
    "id": {'type': 'number'},
    "category": {'type': 'dict'},
    "name": {'type': 'string'},
    "photoUrls": {'type': 'list'},
    "tags": {'type': 'list'},
    "status": {'type': 'string'}
}

pet_client = PetClient()

def test_new_pet_can_be_added():
    pet_id, response = pet_client.create_pet()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    pet = pet_client.get_pet_by_id(pet_id).as_dict
    print(pet)
    assert_that(pet).is_not_empty()

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
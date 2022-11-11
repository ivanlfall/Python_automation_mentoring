import requests
from assertpy import assert_that

from core.api_wrappers.pet_client import PetClient
from core.assertions.custom_assertions import assert_that_body_content_are_equals, assert_that_is_the_correct_schema, \
    assert_successful_operation
from utilities.get_me import Factory
from utilities.print_with_format import print_test_info_with_schema

_factory = Factory()
pet_client = PetClient()
schema = {
    "id": {'type': 'number'},
    "category": {'type': 'dict'},
    "name": {'type': 'string'},
    "photoUrls": {'type': 'list'},
    "tags": {'type': 'list'},
    "status": {'type': 'string'}
}


def test_new_pet_can_be_added():

    pet = _factory.get_me(Factory.PET)
    _, response = pet_client.create_pet(pet)
    assert_successful_operation(response)

    assert_that_body_content_are_equals(pet.__dict__, response.as_dict)


def test_pet_without_name_cannot_be_added():

    pet = _factory.get_me(Factory.PET)
    pet.name = ""
    _, response = pet_client.create_pet(pet)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)


def test_pet_without_photo_cannot_be_added():

    pet = _factory.get_me(Factory.PET)
    pet.photoUrls = None
    _, response = pet_client.create_pet(pet)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)


def test_created_pet_can_be_deleted():
    pet, response = pet_client.create_pet()
    response = pet_client.delete_pet_by_id(pet.id)
    assert_successful_operation(response)

    check_pet = pet_client.get_pet_by_id(pet.id)
    assert_that(check_pet.status_code).is_equal_to(requests.codes.not_found)


def test_read_one_operation_has_expected_schema():
    new_pet, _ = pet_client.create_pet()
    pet = pet_client.get_pet_by_id(new_pet.id)
    print_test_info_with_schema(pet.endpoint, pet.as_dict, schema)

    assert_that_is_the_correct_schema(schema, pet.as_dict)

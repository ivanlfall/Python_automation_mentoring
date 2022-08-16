from assertpy import assert_that, soft_assertions
from cerberus import Validator


def assert_that_body_content_are_equals(send_body, response_body):
    with soft_assertions():
        for key_send_value, key_response_value in zip(send_body.keys(), response_body.keys()):
            assert_that(send_body[key_response_value], key_send_value).is_equal_to(response_body[key_response_value])




def assert_that_is_the_correct_schema(schema, entity):
    validator = Validator(schema)
    is_valid = validator.validate(entity)

    assert_that(is_valid, validator.errors).is_true()
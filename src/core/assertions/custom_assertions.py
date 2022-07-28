from assertpy import assert_that
from cerberus import Validator


def assert_that_body_content_are_equals(send_body, response_body):

    for send_value, response_value in zip(send_body.values(), response_body.values()):
        assert_that(send_value).is_equal_to(response_value)




def assert_that_is_the_correct_schema(schema, entity):

    validator = Validator(schema)
    is_valid = validator.validate(entity)

    assert_that(is_valid, description=validator.errors).is_true()
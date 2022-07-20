from assertpy import assert_that


def assert_that_body_content_are_equals(send_body, response_body):
    result = True

    for send_value, response_value in zip(send_body.values(), response_body.values()):
        if send_value != response_value:
            result = False

    assert_that(result).is_true()
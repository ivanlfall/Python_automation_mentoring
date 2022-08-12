import json


def print_test_info(sent_body, response_body, response_code):
    final_message = {
        'response_code': response_code,
        'sent_body': sent_body,
        'response_body': response_body
    }

    print(json.dumps(final_message, indent=4, sort_keys=False))


def print_test_info_with_schema(response_body, schema):
    final_message = {
        'response_body': response_body,
        'schema': schema,
    }

    print(json.dumps(final_message, indent=4))
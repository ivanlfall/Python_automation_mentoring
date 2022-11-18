import json
from datetime import datetime


def print_request_info(response):

    date_time = f'{datetime.now().strftime("%d/%m/%Y_%H:%M:%S")}'
    verb = response.request.method
    url = response.request.url
    header = response.request.headers
    request_body = response.request.body
    response_code = response.status_code
    response_body = response.text
    elapsed_time = response.elapsed
    size = len(response.content)
    final_message = f"""
    {date_time}
    ************************************************************************
    {verb} / {url}
    Request headers: {header}
    Request body: {request_body}
    Response code: {response_code}
    Response body: {response_body}
    Elapsed time: {elapsed_time} - Size: {size} bytes
    ************************************************************************
    """

    print(final_message)


def print_test_info_with_schema(endpoint, response_body, schema):
    final_message = {
        'endopoint': endpoint,
        'response_body': response_body,
        'schema': schema,
    }

    print(json.dumps(final_message, indent=4))


def print_sent_payload_from_object(sent_object):
    print("\nSent payload: ")
    print(json.dumps(sent_object.__dict__, indent=4))
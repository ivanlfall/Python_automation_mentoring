import json


def print_request_info(response):

    date_time = response.headers["Date"]
    verb = response.request.method
    url = response.request.url
    header = response.request.headers
    request_body = json.loads(response.request.body) if response.request.body else {}
    response_code = response.status_code
    response_body = json.loads(response.text) if response.text else {}
    elapsed_time = response.elapsed
    size = len(response.content)
    final_message = f"""
    {date_time}
    ************************************************************************
    {verb} / {url}
    Request headers: {header}
    Request body: {json.dumps(request_body, indent=8, sort_keys=False)}
    Response code: {response_code}
    Response body: {json.dumps(response_body, indent=8, sort_keys=False)}
    Elapsed time: {elapsed_time}, {size} bytes
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
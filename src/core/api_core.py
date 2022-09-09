from dataclasses import dataclass
from json import JSONDecodeError

import requests


@dataclass
class Response:
    endpoint: str
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    def get(self, url):
        response = requests.get(url)
        return self.__get_responses(response, url)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response, url)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_responses(response, url)

    def __get_responses(self, response, endpoint):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except JSONDecodeError:
            as_dict = None

        headers = response.headers

        return Response(
            endpoint, status_code, text, as_dict, headers
        )

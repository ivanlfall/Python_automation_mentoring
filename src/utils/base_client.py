from core.api_core import APIRequest


class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.request = APIRequest()
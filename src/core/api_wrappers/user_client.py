from json import dumps

from core.api_wrappers.base_client import BaseClient
from resources.urls import BASE_URL
from utilities.get_me import Factory


class UserClient(BaseClient):

    _factory = Factory()

    def __init__(self):
        super().__init__()
        self.base_url = f'{BASE_URL}/user'

    def create_user(self, body=None):
        if body is None:
            new_user = self._factory.get_me(Factory.USER)
        else:
            new_user = body
        payload = dumps(new_user.__dict__)
        response = self.request.post(self.base_url, payload, self.headers)
        return new_user, response

    def get_user_by_username(self, username):
        url = f'{self.base_url}/{username}'
        return self.request.get(url)

    def delete_user_by_username(self, username):
        url = f'{self.base_url}/{username}'
        return self.request.delete(url)

    def login_user(self, username, password):
        url = f'{self.base_url}/login?username={username}&password={password}'
        return self.request.get(url)
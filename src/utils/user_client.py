from json import dumps

from config import BASE_URL
from utils.base_client import BaseClient
from utils.helpers.get_me import Factory


class UserClient(BaseClient):

    _factory = Factory()

    def __init__(self):
        super().__init__()

        self.base_url = f'{BASE_URL}/user'

    def create_user(self, body=None):
        if body is None:
            user_name, new_user = self._factory.get_me(Factory.USER)
            payload = dumps(new_user)
        else:
            payload = dumps(body)
            user_name = body['username']

        response = self.request.post(self.base_url, payload, self.headers)
        return user_name, response

    def get_user_by_username(self, username):
        url = f'{self.base_url}/{username}'
        return self.request.get(url)

    def delete_user_by_username(self, username):
        url = f'{self.base_url}/{username}'
        return self.request.delete(url)
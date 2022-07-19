from json import dumps

from config import BASE_URL
from core.api_core import APIRequest
from utils.base_client import BaseClient
from utils.helpers.get_me import Factory


class UserClient(BaseClient):

    _factory = Factory()

    def __init__(self):
        super().__init__()

        self.base_url = f'{BASE_URL}/user'
        self.request = APIRequest()

    def create_user(self, body=None):
        user_name, new_user = self._factory.get_me(Factory.USER)

        payload = dumps(new_user)

        response = self.request.post(self.base_url, payload, self.headers)
        return user_name, response

    def get_pet_by_username(self, username):
        url = f'{self.base_url}/{username}'
        return self.request.get(url)

    # def delete_pet_by_id(self, pet_id):
    #     url = f'{self.base_url}/{pet_id}'
    #     return self.request.delete(url)
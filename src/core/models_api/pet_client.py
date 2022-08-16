import json
from json import dumps

from config import BASE_URL
from core.models_api.base_client import BaseClient
from utils.helpers.get_me import Factory


class PetClient(BaseClient):

    _factory = Factory()

    def __init__(self):
        super().__init__()
        self.base_url = f'{BASE_URL}/pet'

    def create_pet(self, body=None):
        if body is None:
            new_pet = self._factory.get_me(Factory.PET)
            payload = dumps(new_pet)
        else:
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return json.loads(payload), response

    def get_pet_by_id(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.get(url)

    def delete_pet_by_id(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.delete(url)
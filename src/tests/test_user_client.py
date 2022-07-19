import requests
from assertpy import assert_that

from utils.user_client import UserClient

user_client = UserClient()

def test_new_user_can_be_added():
    user_name , response = user_client.create_user()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    user = user_client.get_pet_by_username(user_name).as_dict
    assert_that(user).is_not_empty()
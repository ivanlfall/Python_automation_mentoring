import random
from faker import Faker

class Factory:

    fake = Faker()

    PET = 'pet'
    STORE = 'store'
    USER = 'user'

    def get_me(self, an_object):

        match an_object:
            case Factory.PET:
                return self.__get_me_a_pet()
            case Factory.USER:
                return self.__get_me_a_user()
            case default:
                return None

    def __get_me_a_pet(self):
        random_id = random.randint(0, 1000)
        return random_id, {
                "id": random_id,
                "category": {
                    "id": 1,
                    "name": "Dog"
                },
                "name": "Corbata",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "Little"
                    }
                ],
                "status": "available"
        }

    def __get_me_a_user(self):
        random_id = random.randint(0, 1000)
        user_name = self.fake.user_name()
        return user_name, {
                  "id": random_id,
                  "username": user_name,
                  "firstName": self.fake.first_name(),
                  "lastName": self.fake.last_name(),
                  "email": self.fake.email(),
                  "password": self.fake.password(),
                  "phone": self.fake.phone_number(),
                  "userStatus": 0
                }

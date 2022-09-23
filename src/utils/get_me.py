from faker import Faker

from resources.data import animal


class Factory:

    fake = Faker()

    PET = 'pet'
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
        return {
                "id": self.fake.unique.random_int(min=0, max=99999),
                "category": {
                    "id": self.fake.unique.random_int(min=0, max=9999),
                    "name": self.fake.random_element(animal)
                },
                "name": self.fake.first_name(),
                "photoUrls": [
                    self.fake.file_name(category='image')
                ],
                "tags": [
                    {
                        "id": self.fake.unique.random_int(min=0, max=9999),
                        "name": ""
                    }
                ],
                "status": self.fake.random_element(['available', 'pending', 'sold'])
        }

    def __get_me_a_user(self):
        return {
                  "id": self.fake.unique.random_int(min=0, max=99999),
                  "username": self.fake.user_name(),
                  "first_name": self.fake.first_name(),
                  "last_name": self.fake.last_name(),
                  "email": self.fake.email(),
                  "password": self.fake.password(),
                  "phone": self.fake.phone_number(),
                  "userStatus": 0
                }
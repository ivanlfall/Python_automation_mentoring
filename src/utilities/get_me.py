from faker import Faker

from core.models.pet import Pet
from core.models.user import User
from core.models.user_for_register import UserForRegister
from resources.data import animal
from utilities.print_with_format import print_sent_payload_from_object


class Factory:

    fake = Faker()

    PET = 'pet'
    USER = 'user'
    USER_FOR_REGISTER = 'user_for_register'

    def get_me(self, an_object):

        match an_object:
            case Factory.PET:
                return self.__get_me_a_pet()
            case Factory.USER:
                return self.__get_me_a_user()
            case Factory.USER_FOR_REGISTER:
                return self.__get_me_a_user_for_register()
            case _:
                return None

    def __get_me_a_pet(self):
        pet_id = self.fake.unique.random_int(min=0, max=99999)
        category = {
            "id": self.fake.unique.random_int(min=0, max=9999),
            "name": self.fake.random_element(animal)
        }
        name = self.fake.first_name()
        photo_urls = [self.fake.file_name(category='image')]
        tags = [{
                "id": self.fake.unique.random_int(min=0, max=9999),
                "name": f"#{category['name']}"
            }]
        status = self.fake.random_element(['available', 'pending', 'sold'])

        return Pet(pet_id, category, name, photo_urls, tags, status)

    def __get_me_a_user(self):
        user_id = self.fake.unique.random_int(min=0, max=99999)
        username = self.fake.user_name()
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        email = self.fake.email()
        password = self.fake.password()
        phone = self.fake.phone_number()

        return User(user_id, username, first_name, last_name, email, password, phone)

    def __get_me_a_user_for_register(self):
        user_id = self.fake.user_name()
        password = self.fake.password()
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        email = self.fake.email()
        phone = self.fake.phone_number()
        address = self.fake.street_address()
        city = self.fake.city()
        state = self.fake.state()
        zip_code = self.fake.postcode()
        country = self.fake.country()
        user = UserForRegister(user_id, password, first_name, last_name, email, phone, address,
                               city, state, zip_code, country)
        print_sent_payload_from_object(user)

        return user

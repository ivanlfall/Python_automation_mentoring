from core.page_models.regiter_user_pet_store import RegisterPage
from faker import Faker

fake = Faker()


def test_user_can_register(driver):
    register_page = RegisterPage(driver)

    user_id = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address()
    city = fake.city()
    state = fake.state()
    zip_code = fake.post_code()
    country = fake.country()

    register_page.create_account(user_id, password, password, first_name, last_name, email,
                                 phone, address, city, state, zip_code, country)
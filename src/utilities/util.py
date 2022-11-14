from utilities.get_me import Factory


def create_account(register_page):
    factory = Factory()
    user = factory.get_me(Factory.USER_FOR_REGISTER)

    register_page.load()
    register_page.username_input().insert_value(user.id)
    register_page.password_input().insert_value(user.password)
    register_page.repeat_password_input().insert_value(user.password)
    register_page.first_name_input().insert_value(user.first_name)
    register_page.last_name_input().insert_value(user.last_name)
    register_page.email_input().insert_value(user.email)
    register_page.phone_input().insert_value(user.phone)
    register_page.address_input().insert_value(user.address)
    register_page.city_input().insert_value(user.city)
    register_page.state_input().insert_value(user.state)
    register_page.zip_code_input().insert_value(user.zip_code)
    register_page.country_input().insert_value(user.country)
    register_page.create_account_button().click()

    return user.id, user.password
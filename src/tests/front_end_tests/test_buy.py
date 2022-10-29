import pytest
from assertpy import assert_that

from utilities.util import create_account

DOG_BREEDS = ["Bulldog", "Chihuahua", "Dalmation"]
CAT_BREEDS = ["Manx", "Persian"]


@pytest.mark.parametrize("breed", DOG_BREEDS)
def test_buy_a_dog(breed, index_home, animal_catalog, specific_breed_catalog, animal_info,
                   shopping_cart, buy_details, confirm_order, confirmation_buy_summary):
    index_home.load()
    index_home.side_bar_dogs_button().click()
    animal_catalog.animal_breed_choice(breed).click()
    dog_item = specific_breed_catalog.pet_item()
    dog_item_text = dog_item.get_inner_text()
    dog_item.click()
    animal_info.add_to_card_button().click()
    shopping_cart.proceed_to_checkout().click()
    buy_details.continue_button().click()
    confirm_order.confirm_button().click()

    message = confirmation_buy_summary.confirmation_message().get_inner_text()
    assert_that(message).contains("order has been submitted")
    assert_buy(dog_item_text, confirmation_buy_summary.bought_items())


@pytest.mark.parametrize("breed", CAT_BREEDS)
def test_buy_a_cat(breed, index_home, animal_catalog, specific_breed_catalog, animal_info,
                   shopping_cart, buy_details, confirm_order, confirmation_buy_summary):
    index_home.load()
    index_home.side_bar_cats_button().click()
    animal_catalog.animal_breed_choice(breed).click()
    cat_item = specific_breed_catalog.pet_item()
    cat_item_text = cat_item.get_inner_text()
    cat_item.click()
    animal_info.add_to_card_button().click()
    shopping_cart.proceed_to_checkout().click()
    buy_details.continue_button().click()
    confirm_order.confirm_button().click()

    message = confirmation_buy_summary.confirmation_message().get_inner_text()
    assert_that(message).contains("order has been submitted")
    assert_buy(cat_item_text, confirmation_buy_summary.bought_items())


def assert_buy(purchase, buy_summary):
    assert_that(buy_summary).extracting('get_inner_text').contains(purchase)


@pytest.fixture(autouse=True)
def login_before_test(index_home, sign_in_page, register_page, home_after_login):
    if not home_after_login.sign_out_button().is_present():
        username, password = create_account(register_page)
        index_home.sign_in_button().click()
        sign_in_page.username_input().insert_value(username)
        sign_in_page.password_input().insert_value(password)
        sign_in_page.login_button().click()
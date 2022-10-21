import random
import string


def get_name_from_locator(locator):
    if '"' in locator:
        start = locator.find('"') + 1
        end = locator.rfind('"')
        return locator[start:end]
    elif '=' in locator:
        start = locator.find('=') + 1
        end = locator.find(']')
        return locator[start:end]
    else:
        return locator


def get_random_text():
    number_of_char = 10
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=number_of_char))
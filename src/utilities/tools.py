import random
import string


def get_random_text(max_length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=max_length))


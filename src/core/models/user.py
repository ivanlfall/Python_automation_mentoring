

class User:
    def __init__(self, user_id, username, first_name, last_name, email, password, phone):
        self.id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = 0

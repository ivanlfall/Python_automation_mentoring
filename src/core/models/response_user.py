
class ResponseUser:

    def __init__(self, status, message, user_id, first_name, last_name):
        self.__status = status
        self.__message = message
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name

    def get_user(self):
        return {
            'status': self.__status,
            'message': self.__message,
            'id': self.__user_id,
            'first_name': self.__first_name,
            'last_name': self.__last_name
        }

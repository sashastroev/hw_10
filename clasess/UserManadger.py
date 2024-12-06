from .User import User
from .UserExeptions import UserAlreadyExistsError, UserNotFoundError

class UserManadger:
    users = {}
    
    # def __init__(self):
    #     pass

    @staticmethod
    def add_user(user: User):
        if not user.username in UserManadger.users:
            UserManadger.users[user.username] = user
        else: 
            print(UserAlreadyExistsError(user.username))

    @staticmethod
    def remove_user(username: str):
        try:
            UserManadger.users.pop(username)
        except KeyError: 
            print(UserNotFoundError(username))

    @staticmethod
    def find_user(username: str)-> User:
        try:
            return UserManadger.users[username]
        except KeyError: 
            raise UserNotFoundError(username)

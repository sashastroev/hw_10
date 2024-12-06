class UserAlreadyExistsError(Exception):
    def __init__(self, username, message='Пользоатель с таким именем уже зарегистрирован'):
        super().__init__(message)
        self.username = username
        self.message = message
    
    def __str__(self):
        return f'{self.message}: {self.username}'
    

class UserNotFoundError(Exception):
    def __init__(self, username, message='Пользоатель с таким именем не найден'):
        super().__init__(message)
        self.username = username
        self.message = message
    
    def __str__(self):
        return f'{self.message}: {self.username}'

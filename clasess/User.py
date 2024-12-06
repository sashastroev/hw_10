class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f'\nИмя: {self.username}\nПочта: {self.email}\nВозраст: {self.age}'
    
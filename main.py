from clasess.User import User
from clasess.UserManadger import UserManadger


# Создадим пользователя и выведем его
user1 = User('Andey', 'and@and.ru', 25)
print(user1)

# Добавим пользователя
UserManadger.add_user(user1)
print(UserManadger.users)

# Пробуем добавить пользователя с таким же именем
UserManadger.add_user(user1)

# Пробуем удалить пользователя по несуществующему имени
UserManadger.remove_user('Maxim')

# Пробуем получить пользователя по несуществующему имени
UserManadger.find_user('Alex')

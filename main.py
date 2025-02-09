class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Инкапсуляция: защищенный атрибут
        self._name = name        # Инкапсуляция: защищенный атрибут
        self._access_level = "user"  # Уровень доступа по умолчанию

    # Геттеры для доступа к защищенным атрибутам
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Сеттер для изменения имени
    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"  # Переопределение уровня доступа для администратора
        self._users = []  # Список для хранения пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Некорректный объект пользователя.")

    # Метод для удаления пользователя по ID
    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь с ID {user_id} успешно удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для отображения всех пользователей
    def list_users(self):
        if not self._users:
            print("В системе нет пользователей.")
        else:
            print("Пользователи в системе:")
            for user in self._users:
                print(user)


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(1, "Анна")

    # Создаем обычных пользователей
    user1 = User(2, "Иван")
    user2 = User(3, "Алексей")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Выводим список пользователей
    admin.list_users()

    # Администратор удаляет пользователя
    admin.remove_user(2)

    # Снова выводим список пользователей
    admin.list_users()
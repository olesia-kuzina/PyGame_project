import sqlite3


class DataBase:  # класс базы данных
    def __init__(self):  # конструктор класса
        self.connection = sqlite3.connect('DB.sqlite')
        self.cursor = self.connection.cursor()

    def __del__(self):  # "прекращает" работу после окончания работы главного приложения
        self.connection.close()

    def add_user(self, name):  # добавление нового польхователя в базу данных по имени
        user_names = [i[0] for i in self.cursor.execute("""SELECT user_name FROM user""").fetchall()]
        if name not in user_names:
            self.cursor.execute("""INSERT INTO user (user_name) VALUES (?)""", (name,))
            self.connection.commit()

    def get_user_by_name(self, name):  # получение всей информации о пользователе по имени
        user = self.cursor.execute("""SELECT * FROM user WHERE user_name = ? """, (name,)).fetchone()
        if not user:
            self.add_user(name)
            return self.get_user_by_name(name)
        return user

    def deletes(self, name):  # удаление пользователя
        self.cursor.execute("""DELETE FROM user WHERE user_name = ?""", (name,))
        self.connection.commit()

    def update_score(self, score,
                     name):  # обновление информации о пользователе в базе данных (новый рекорд (если он есть) и
        # увелечение количества всех яблочек)
        user = self.get_user_by_name(name)
        if user[2] < score:
            self.cursor.execute("""UPDATE user SET score = ? WHERE user_name = ?""", (score, name))
            self.connection.commit()
        self.cursor.execute("""UPDATE user SET count_of_apple = ? WHERE user_name = ?""", (user[3] + score, name))
        self.connection.commit()


if __name__ == "__main__":
    db = DataBase()

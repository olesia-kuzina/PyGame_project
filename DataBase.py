import sqlite3


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('DB.sqlite')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def add_user(self, name):
        user_names = [i[0] for i in self.cursor.execute("""SELECT user_name FROM user""").fetchall()]
        if name not in user_names:
            self.cursor.execute("""INSERT INTO user (user_name) VALUES (?)""", (name,))
            self.connection.commit()

    def get_user_by_name(self, name):
        user = self.cursor.execute("""SELECT * FROM user WHERE user_name = ? """, (name,)).fetchone()
        return user

    def deletes(self, name):
        self.cursor.execute("""DELETE FROM user WHERE user_name = ?""", (name,))
        self.connection.commit()


if __name__ == "__main__":
    db = DataBase()
import random
import sys

import pygame
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow

from DataBase import DataBase
from models import Board, Snake, Apple, Star
from ui.window import Ui_MainWindow


class WindowInterface:  # класс для взаимодействия с окном
    def set_score(self, score: int):  # определяем метод set_score
        pass

    def end_game(self, score: int):  # определяем метод end_game
        pass


class Game:
    def __init__(self, window: WindowInterface, btn_txt: str):
        pygame.init()
        self.window = window

        self.cell_size = 30
        self.grid_width, self.grid_height = 10, 10
        self.screen_width = self.grid_width * self.cell_size
        self.screen_height = self.grid_height * self.cell_size

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        if btn_txt == 'low':  # если пользователь нажимает на кнопку с текстом 'low'
            self.fps = 3  # устанавливаем небольшую скорость
        elif btn_txt == 'medium':  # если пользователь нажимает на кнопку с текстом "medium"
            self.fps = 6  # устанавливаем среднюю скорость
        else:  # в противном случае
            self.fps = 9  # устанавливаем быструю скорость
        self.board = Board(height=self.grid_height, width=self.grid_width, cell_size=self.cell_size)
        self.snake = Snake(cell_size=self.cell_size)
        self.apple = Apple(self.grid_width, self.grid_height, self.cell_size, self.snake.body)
        self.stars_group = pygame.sprite.Group()  # грцппа для звездочек

    def loop(self, playing: bool):  # метод loop обрабатывает события pygame
        if not playing:  # если игра не открыта
            return False  # возвращаем False

        for event in pygame.event.get():  # обрабатываем eventы
            if event.type == pygame.QUIT:  # если окно закрывается
                self.window.end_game(self.snake.get_score())  # передаём в окно кол-во очков при окончании игры
                return True  # возвра
            elif event.type == pygame.KEYDOWN:  # если происходит опусание какой-то кнопочки
                if event.key == pygame.K_UP:  # и это стрелочка вниз
                    self.snake.new_direction((0, -1))  # изменяем направление
                elif event.key == pygame.K_DOWN:  # если это стрелочка вниз
                    self.snake.new_direction((0, 1))  # изменяем направление и тд
                elif event.key == pygame.K_LEFT:
                    self.snake.new_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.new_direction((1, 0))
        self.snake.move()  # устанавливаем новое расположение змейки
        if self.apple.position == self.snake.body[0]:  # если голова "съедает" яблоко
            stars_count = 10  # кол-во звезд
            numbers = range(-5, 6)  # рандомное направление
            for _ in range(stars_count):
                Star((self.screen_width // 2, self.screen_height // 2), (0, 0, self.screen_width, self.screen_height),
                     random.choice(numbers), random.choice(numbers), self.stars_group)
            self.snake.grow()  # увеличиваем тело змеи
            self.window.set_score(self.snake.get_score())
            self.apple.position = self.apple.generate_position(self.snake.body)  # устанавливаем новую позицию яблочка
        else:
            if self.snake.check_collision(width=self.grid_width,
                                          height=self.grid_height):  # если происходит столкновение
                self.window.end_game(self.snake.get_score())
                return True

        self.screen.fill((252, 186, 3))  # закрашиваем экран
        self.board.render(self.screen)  # отрисовка
        self.snake.render(self.screen)  # отрисовка
        self.apple.render(self.screen)  # отрисовка
        self.stars_group.update()  # обновляем группу со звездами
        self.stars_group.draw(self.screen)  # отрисовываем звезды
        pygame.display.flip()  # обновляем содержимое окна
        self.clock.tick(self.fps)
        return False


class Window(QMainWindow, WindowInterface):
    def __init__(self):
        super().__init__()
        self.title = "Snake"
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.init_ui()
        self.set_callbacks()

        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

        self.playing = False
        self.db = DataBase()

    def set_callbacks(self):  # в этом методе вызываются методы, которые срабатывают при нажатии на кнопки в Qt
        self._ui.btnLogin.clicked.connect(self.login)
        self._ui.btnExit.clicked.connect(self.close)
        self._ui.btnLow.clicked.connect(self.init_pygame)
        self._ui.btnMedium.clicked.connect(self.init_pygame)
        self._ui.btnHard.clicked.connect(self.init_pygame)
        self._ui.btnMenu.clicked.connect(self.to_menu)

    def init_ui(self):  # метод для работы с окнами Qt
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.stackedWidget.setCurrentIndex(1)

        self.show()

    def init_pygame(self):  # метод для запуска pygame
        button_txt = self.sender().text()  # получаем текст с нажатой кнопки в окне Qt
        self.game = Game(self, button_txt)
        self.playing = True
        self._ui.stackedWidget.setCurrentIndex(
            3)  # открываем 4 страницу с индексом 3 (индексация страниц с 0) во время игры

    def pygame_loop(self):  # заставляет pygame обрабатывать события
        if not self.playing:  # если игра не запущена
            return  # ничего не происходит
        if self.game.loop(self.playing):  # если игра закончилась
            pygame.quit()  # закрывает окно pygame
            self.playing = False  # флаг становится отрицательным, показывая, что игра остановлена
            self._ui.stackedWidget.setCurrentIndex(2)  # переключаемся на заключительную страницу в Qt

    def login(self):  # метотд для регистрации/захода в имеющийся аккаунт пользователя
        username = self._ui.editLogin.text()
        self.user = list(self.db.get_user_by_name(username))
        self.update_info()
        self._ui.stackedWidget.setCurrentIndex(0)

    def update_info(self):  # изменяем информацию о пользователе
        self._ui.labelUsername.setText(f"name: {self.user[1]}\n"
                                       f"record: {self.user[2]}\n"
                                       f"total apple: {self.user[3]}")

    def to_menu(self):  # возвращаемся в меню
        self._ui.stackedWidget.setCurrentIndex(0)

    def set_score(self, score: int):  # изменяет рекорд
        self._ui.count.display(str(score))

    def end_game(self, score: int):  # конец игры
        self._ui.label.setText(f"End Game! Your score: {score}")
        self.db.update_score(score, self.user[1])
        self.user = list(self.db.get_user_by_name(self.user[1]))  # обновление информации в self.user
        self.update_info()


def main():  # запуск приложения
    app = QApplication(sys.argv)
    window = Window()
    result = app.exec()
    sys.exit(result)


if __name__ == "__main__":
    main()

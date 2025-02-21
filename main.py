import random
import sys

import pygame
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow

from models import Board, Snake, Apple, Star
from ui.window import Ui_MainWindow


class WindowInterface:  # класс для взаимодействия с окном
    def set_score(self, score: int):  # определяем метод set_score
        pass

    def end_game(self, score: int):  # определяем метод end_game
        pass


class Game:
    def __init__(self, window: WindowInterface):
        pygame.init()
        self.window = window

        self.cell_size = 30
        self.grid_width, self.grid_height = 10, 10
        self.screen_width = self.grid_width * self.cell_size
        self.screen_height = self.grid_height * self.cell_size

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.fps = 3
        self.board = Board(height=self.grid_height, width=self.grid_width, cell_size=self.cell_size)
        self.snake = Snake(cell_size=self.cell_size)
        self.apple = Apple(self.grid_width, self.grid_height, self.cell_size, self.snake.body)
        self.stars_group = pygame.sprite.Group()

    def loop(self, playing: bool):  # метод loop обрабатывает события pygame
        if not playing:
            return False

        for event in pygame.event.get():  # обрабатываем eventы
            if event.type == pygame.QUIT:  # если окно закрывается
                self.window.end_game(self.snake.get_score())  # передаём в окно кол-во очков при окончании игры
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.new_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.new_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.new_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.new_direction((1, 0))
        self.snake.move()  # устанавливаем новое расположение змейки
        if self.apple.position == self.snake.body[0]:  # если голова "съедает" яблоко
            stars_count = 10  # кол-во звезд
            numbers = range(-5, 6)
            for _ in range(stars_count):
                Star((self.screen_width // 2, self.screen_height // 2), (0, 0, self.screen_width, self.screen_height),
                     random.choice(numbers), random.choice(numbers), self.stars_group)
            self.snake.grow()
            self.window.set_score(self.snake.get_score())
            self.apple.position = self.apple.generate_position(self.snake.body)
        else:
            if self.snake.check_collision(width=self.grid_width, height=self.grid_height):
                self.window.end_game(self.snake.get_score())
                return True

        self.screen.fill((252, 186, 3))
        self.board.render(self.screen)
        self.snake.render(self.screen)
        self.apple.render(self.screen)
        self.stars_group.update()
        self.stars_group.draw(self.screen)
        pygame.display.flip()
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

    def set_callbacks(self):
        self._ui.btnLogin.clicked.connect(self.login)
        self._ui.btnExit.clicked.connect(self.close)
        self._ui.btnLow.clicked.connect(self.init_pygame)
        self._ui.btnMedium.clicked.connect(self.init_pygame)
        self._ui.btnHard.clicked.connect(self.init_pygame)
        self._ui.btnMenu.clicked.connect(self.to_menu)

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.stackedWidget.setCurrentIndex(1)

        self.show()

    def init_pygame(self):
        self.game = Game(self)
        self.playing = True
        self._ui.stackedWidget.setCurrentIndex(3)

    def pygame_loop(self):
        if not self.playing:
            return
        if self.game.loop(self.playing):
            pygame.quit()
            self.playing = False
            self._ui.stackedWidget.setCurrentIndex(2)

    def login(self):
        username = self._ui.editLogin.text()
        self._ui.labelUsername.setText(username)
        self._ui.stackedWidget.setCurrentIndex(0)

    def to_menu(self):
        self._ui.stackedWidget.setCurrentIndex(0)

    def set_score(self, score: int):
        self._ui.count.display(str(score))

    def end_game(self, score: int):
        self._ui.label.setText(f"End Game! Your score: {score}")


def main():
    app = QApplication(sys.argv)
    window = Window()
    result = app.exec()
    sys.exit(result)


if __name__ == "__main__":
    main()

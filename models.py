import pygame
import random

from pygame.sprite import Group


class Board:  # класс доски
    def __init__(self, height: int, width: int, cell_size: int,
                 grid_color: tuple[int, int, int] = (255, 255, 255)):  # конструктор класса
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.grid_color = grid_color

    def render(self, screen):  # отрисовщик
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, self.grid_color, (x * self.cell_size, y * self.cell_size, self.cell_size,
                                                           self.cell_size), 2)


class Snake:  # класс змейки
    def __init__(self, cell_size: int, color: tuple[int, int, int] = (0, 255, 0),
                 start_pos: tuple[int, int] = (5, 5)):  # конструктор
        self.cell_size = cell_size
        self.color = color
        self.start_pos = start_pos
        self.body = [start_pos]
        self.direction = (1, 0)

    def render(self, screen):  # отрисовщик
        for i in self.body:
            pygame.draw.rect(screen, self.color, (i[0] * self.cell_size, i[1] * self.cell_size, self.cell_size,
                                                  self.cell_size))

    def move(self):  # движение змейки
        x_head, y_head = self.body[0]
        x_direction, y_direction = self.direction
        new_head = (x_head + x_direction, y_head + y_direction)
        self.body.insert(0, new_head)
        self.body.pop()

    def new_direction(self, new_dir):  # изменяет направление
        if (self.direction[0] + new_dir[0] != 0) or (self.direction[1] + new_dir[1] != 0):
            self.direction = new_dir

    def check_collision(self, width: int, height: int):  # проверка на столкновение со сеной или с самой собой
        if not (0 <= self.body[0][0] < width and 0 <= self.body[0][-1] < height):
            return True
        elif self.body[0] in self.body[1:]:
            return True
        return False

    def grow(self):  # рост змейки при съедеии яблочек
        self.body.append(self.body[-1])

    def get_score(self):  # получение кол-ва очков
        return len(self.body) - 1


class Apple:  # класс яблок
    def __init__(self, grid_width: int, grid_height: int, cell_size: int, body_snake: list):  # конструктор
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.position = self.generate_position(body_snake)

    def generate_position(self, body_snake: list):  # генерирует рандомную позицию яблока
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in body_snake:
                return x, y

    def render(self, screen):  # отрисовщик
        pygame.draw.circle(screen, 'red', (self.position[0] * self.cell_size + self.cell_size // 2,
                                           self.position[1] * self.cell_size + self.cell_size // 2),
                           self.cell_size // 2)


class Star(pygame.sprite.Sprite):  # класс звезд

    def __init__(self, pos: tuple, screen_rect: tuple, dx: int, dy: int, stars_sprite: Group):  # конструктор
        super().__init__(stars_sprite)
        self.add(stars_sprite)  # добавляем в группу для спрайтов звезды
        self.screen_rect = screen_rect  # сохраняем прямоугольник экрана
        self.image = pygame.image.load('star.png')  # загружаем картинку
        self.rect = self.image.get_rect()  # сохряняем размеры прямоугольника, в который заключена картинка
        self.velocity = [dx, dy]  # у каждой звезды своя скорость (вектор)
        self.rect.x, self.rect.y = pos  # задаем координаты звезде
        self.gravity = 4  # гравитация

    def update(self):  # "двигает звездочку" изменяет положение
        self.velocity[1] += self.gravity  # увеличиваем скорость
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(self.screen_rect):  # если частица вне экрана
            self.kill()  # убиваем её

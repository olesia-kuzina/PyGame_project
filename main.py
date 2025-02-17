import pygame
import random


class Board:
    def __init__(self, height: int, width: int, cell_size: int, grid_color: tuple[int, int, int] = (255, 255, 255)):
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.grid_color = grid_color

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen, self.grid_color, (x * self.cell_size, y * self.cell_size, self.cell_size,
                                                           self.cell_size), 2)


class Snake:
    def __init__(self, cell_size: int, color: tuple[int, int, int] = (0, 255, 0), start_pos: tuple[int, int] = (5, 5)):
        self.cell_size = cell_size
        self.color = color
        self.start_pos = start_pos
        self.body = [start_pos]
        self.direction = (1, 0)

    def render(self, screen):
        for i in self.body:
            pygame.draw.rect(screen, self.color, (i[0] * self.cell_size, i[1] * self.cell_size, self.cell_size,
                                                  self.cell_size))

    def move(self):
        x_head, y_head = self.body[0]
        x_direction, y_direction = self.direction
        new_head = (x_head + x_direction, y_head + y_direction)
        self.body.insert(0, new_head)
        self.body.pop()

    def new_direction(self, new_dir):
        if (self.direction[0] + new_dir[0] != 0) or (self.direction[1] + new_dir[1] != 0):
            self.direction = new_dir

    def check_collision(self, width: int, height: int):
        if not (0 <= self.body[0][0] < width and 0 <= self.body[0][-1] < height):
            return True
        elif self.body[0] in self.body[1:]:
            return True
        return False

    def grow(self):
        self.body.append(self.body[-1])


class Apple:
    def __init__(self, grid_width: int, grid_height: int, cell_size: int, body_snake: list):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        self.position = self.generate_position(body_snake)

    def generate_position(self, body_snake: list):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in body_snake:
                return x, y

    def render(self, screen):
        pygame.draw.circle(screen, 'red', (self.position[0] * self.cell_size + self.cell_size // 2,
                                           self.position[1] * self.cell_size + self.cell_size // 2),
                           self.cell_size // 2)


def main():
    pygame.init()
    cell_size = 30
    grid_width, grid_height = 10, 10
    screen_width = grid_width * cell_size
    screen_height = grid_height * cell_size

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    fps = 3
    board = Board(height=grid_height, width=grid_width, cell_size=cell_size)
    snake = Snake(cell_size=cell_size)
    apple = Apple(grid_width, grid_height, cell_size, snake.body)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.new_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.new_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.new_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.new_direction((1, 0))
        snake.move()
        if apple.position == snake.body[0]:
            print(2)
            snake.grow()
            apple.position = apple.generate_position(snake.body)
        else:
            if snake.check_collision(width=grid_width, height=grid_height):
                running = False
                print('GAME OVER')

        screen.fill((252, 186, 3))
        board.render(screen)
        snake.render(screen)
        apple.render(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()

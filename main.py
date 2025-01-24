import pygame


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


def main():
    pygame.init()
    cell_size = 30
    grid_width, grid_height = 10, 10
    screen_width = grid_width * cell_size
    screen_height = grid_height * cell_size

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    fps = 30
    board = Board(height=grid_height, width=grid_width, cell_size=cell_size)
    snake = Snake(cell_size=cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((252, 186, 3))
        board.render(screen)
        snake.render(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()

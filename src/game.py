import pygame

try:
    from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SPEED, BLACK
except ModuleNotFoundError:
    from config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SPEED, BLACK


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BLACK)
            pygame.display.flip()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()
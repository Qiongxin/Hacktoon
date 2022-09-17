import pygame, sys
from debugging import *
from settings import *
from level import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Magnolia')
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            self.screen.fill('black')
            self.level.run()
            pygame.display.flip()
            self.clock.tick(TICK_SPEED)


if __name__ == "__main__":
    game = Game()
    game.run()
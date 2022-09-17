import pygame, sys
class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group() 
    def run(self):
        pass
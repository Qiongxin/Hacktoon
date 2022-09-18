import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, img):
        super().__init__(groups)
        self.image = pygame.image.load('images/Rock1.png')
        self.rect = self.image.get_rect(topleft = pos)
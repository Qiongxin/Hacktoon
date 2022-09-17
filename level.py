import pygame, sys
from settings import *
from tile import Tile
from player import Player
class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group() 
        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites])
    def run(self):
        self.visible_sprites.draw(self.display)
        self.visible_sprites.update()

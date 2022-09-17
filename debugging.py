import pygame
pygame.init()
font = pygame.font.SysFont('corbel', 20)
def debug_center(text, y):
    screen = pygame.display.get_surface()
    text = font.render(text, True, 'white')
    screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, y))
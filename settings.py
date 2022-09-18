import pygame
TICK_SPEED = 60
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 64
CAPTION = "GAME NAME"
# Tiles are labeled as follows:
# For tiles with grass borders (water, dirt):
# [Type]_[Grass borders]_[Inner corner toggle]
# So a water tile with a border on the top and left, and an inner corner in the bottom right, would be:
# W_G1G2_1
# And a dirt tile with no borders and an inner corner in the top leftwould be:
# D__4
# W = water, D = dirt
# G1-G4 signify grass borders on the North, East, South, and West sides in that order
# The last digit toggles the inner corner for that tile
# A last digit of 0 means no corner
# A value of 1-4 signify a corner in the NE, SE, SW, NW corners in that order

# Tiles without grass borders will be labeled by their actual name:
# Rock1
# Tree2
# etc
WORLD_MAP = [
['W__2','W_3','W_3','W_3','W_3','W_3','W_3','W_3','W_3','W__3'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],    
['x',' ','p',' ',' ',' ',' ',' ',' ','x'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],    
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x'],    
]
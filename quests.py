import pygame
from random import randint

class Quest:
    def __init__(self, questType, text, exp):
        self.questType = questType
        self.text = text
        self.exp = exp

import pygame
from constants import *

pygame.init()

class Minigame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.won = False
        self.color = BLACK
        self.paint()

    def paint(self):
        self.image = pygame.Surface(
            [MINIGAME_WIDTH, MINIGAME_HEIGHT])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image,
                         self.color,
                         [MINIGAME_START_X,
                          MINIGAME_START_Y,
                          MINIGAME_WIDTH,
                          MINIGAME_HEIGHT])
        self.rect = self.image.get_rect()

    def done():
        return won

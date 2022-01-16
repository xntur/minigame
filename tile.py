import pygame
from minigames import clicker, wordguess
from constants import *

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, color):
        super().__init__()

        # Class variables!
        self.minigame = clicker.Clicker()
        self.color = GREY

        self.image = pygame.Surface([TILE_WIDTH, TILE_HEIGHT])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.changecolor(color)
        self.rect = self.image.get_rect()
        
    def changecolor(self, color):
        pygame.draw.rect(self.image, color, [0, 0, TILE_WIDTH, TILE_HEIGHT])

    def handle(self, event):
        if self.minigame.won:
            self.color = BLUE
        self.changecolor(self.color)
        if event.type == pygame.MOUSEBUTTONUP and not self.minigame.won:
            ptx, pty = pygame.mouse.get_pos()
            if self.rect.collidepoint(ptx, pty):
                print("hi")
                return self.minigame
        return None

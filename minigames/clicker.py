import pygame, random
from minigames import minigame
from constants import *

class Clicker(minigame.Minigame):
    def __init__(self):
        super().__init__()
        self.limit = random.randint(5,25)
        self.counter = 0
        self.color = RED
        
    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.counter += 1
            if self.counter >= self.limit:
                self.won = True
        self.paint()
        self.font = pygame.font.SysFont("Impact", 30)
        self.textSurf = self.font.render(
            "CLICK " + str(self.limit - self.counter) + " TIMES!", 1, WHITE) 
        self.image.blit(self.textSurf, [100, 100])

        return self

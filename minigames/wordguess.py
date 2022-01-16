import pygame, random
from minigames import minigame
from constants import *

class WordGuess(minigame.Minigame):
    words = ["HELLO"]

    def __init__(self):
        super().__init__()
        self.word = random.choice(self.words)
        self.color = RED
        self.guess = ''
        self.letters = [' ', ' ' , ' ', ' ', ' ']
        self.count = 5
        
    def handle(self, event):
        if event.type != pygame.KEYDOWN:
            return self

        if event.unicode.isalpha() and len(self.guess) < 5:
            self.guess += event.unicode.upper()

        if event.key == pygame.K_RETURN and len(self.guess) == 5:
            count = 0
            for i in range(0, 5):
                if self.guess[i] == self.word[i]:
                    self.letters[i] = self.guess[i]
                if self.letters[i] == self.word[i]:
                    count += 1
            guess = ''
            if count == 5:
                self.won = True

        if event.key == pygame.K_BACKSPACE and len(self.guess) > 0:
            self.guess = self.guess[:-1]

        self.paint()        
        self.font = pygame.font.SysFont("Impact", 30)
        self.textSurf = self.font.render(
            "GUESS THE WORD!", 1, WHITE)
        self.image.blit(self.textSurf, [100, 100])

        self.textSurf = self.font.render(
            "_ _ _ _ _", 1, WHITE)
        self.image.blit(self.textSurf, [100, 200])

        return self

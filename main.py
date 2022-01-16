#Import the pygame library and initialise the game engine
import pygame

from tile import Tile
from constants import *

# Open a new window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
 
#This will be a list that will contain all the sprites we intend to use in our game.
tile_list = pygame.sprite.Group()
current_sprites = pygame.sprite.Group()
for i in range(0, 16):
    tile = Tile(GREY)
    x = 60 + 100 * (i // 4)
    y = 60 + 100 * (i % 4)
    
    tile.rect.x = x
    tile.rect.y = y
    tile_list.add(tile)
    current_sprites.add(tile)
    
# How long to keep playing the game.
playing = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while playing:
    # --- Main event loop
    mouse = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              playing = False
              break

        next_sprites = current_sprites
        for sprite in current_sprites:
            if type(sprite) == Tile:
                print(id(sprite))
            game = sprite.handle(event)
            if game:
                next_sprites = pygame.sprite.Group()
                print(game.won)
                if game.won:
                    for tile in tile_list:
                        next_sprites.add(tile)
                else:
                    next_sprites.add(game)
        current_sprites = next_sprites
        
    # Drawing code.
    screen.fill(WHITE)
    current_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # Limits FPS

 
# Stop game on quit.
pygame.quit()

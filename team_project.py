import pygame
from pygame import sprite
from stats import Stats
from pygame.draw import rect
from character import Character
from CHARACTER_VARIABLES import *


pygame.init()

win = pygame.display.set_mode((1280, 760))

pygame.display.set_caption("The Legend of the Red Rectangle")

# Red Character and Stats and Movement
red = Character(pygame.image.load('red_sprite/red_right_1.png'),
                RED_WIDTH, RED_HEIGHT, RED_VELOCITY, RED_X, RED_Y)
red_stats = Stats(red)
red.movement_setup("red_sprite", "red")

# Set up the game window
def gameWindow():
    win.fill((0, 0, 0))

    red.showCharacter(win)
    red_stats.show_health_bar(win, red.x, red.y)    

    pygame.display.update()

run = True

# This loop runs the game.
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Get the key pressed from user
    key = pygame.key.get_pressed()

    # Update Character
    red.move(key)

    gameWindow()
    
pygame.quit()
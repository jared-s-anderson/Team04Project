import pygame
from pygame import sprite
from stats import Stats
from pygame.draw import rect


pygame.init()

win = pygame.display.set_mode((1280, 760))

pygame.display.set_caption("The Legend of the Red Rectangle")



# Movement
moveRight = [pygame.image.load('images/Red_sprite_7.png'), 
pygame.image.load('images/Red_sprite_8.png'), pygame.image.load
('images/Red_sprite_9.png')]


moveLeft = [pygame.image.load('images/Red_sprite_4.png'), 
pygame.image.load('images/Red_sprite_5.png'), pygame.image.load
('images/Red_sprite_6.png')]


moveUp = [pygame.image.load('images/Red_sprite_10.png'), 
pygame.image.load('images/Red_sprite_11.png'), pygame.image.load
('images/Red_sprite_12.png')]


moveDown = [pygame.image.load('images/Red_sprite_1.png'), 
pygame.image.load('images/Red_sprite_2.png'), pygame.image.load
('images/Red_sprite_3.png')]

# Starting Red sprite
standing = pygame.image.load('images/Red_sprite_1.png')
pygame.display.set_caption("The Legend of Red Rectangle")

x = 50
y = 50
width = 64
height = 64
vel = 7

# Movement variables
left = False
right = False
up = False
down = False
walk = 0

GREEN_LEFT = 0
TOP = 0
WIDTH = 50
HEIGHT = 8
red_left = 50


def gameWindow():
    win.fill((0, 0, 0))

    global red_left
    health_bar = pygame.Surface((WIDTH, HEIGHT))
    health_bar.fill(pygame.Color("green"), (GREEN_LEFT, TOP, WIDTH, HEIGHT))
    health_bar.fill(pygame.Color("red"), (red_left, TOP, WIDTH, HEIGHT))

    win.blit(health_bar, (x - 10, y - 20))

    global walk
    if walk + 1 >= 12:
        walk = 0
    if right:
        win.blit(moveRight[walk // 4], (x, y))
        walk += 1
        red_left -= 1
    elif left:
        win.blit(moveLeft[walk // 4], (x, y))
        walk += 1
        red_left += 1
    elif up:
        win.blit(moveUp[walk // 4], (x, y))
        walk += 1
    elif down:
        win.blit(moveDown[walk // 4], (x, y))
        walk += 1
    else:
        win.blit(standing, (x, y))
    
    pygame.display.update()


run = True

# This loop runs the game.
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT]:
        x += vel
        left = False
        right = True
        up = False
        down = False
    elif keys[pygame.K_UP]:
        y -= vel
        left = False
        right = False
        up = True
        down = False
    elif keys[pygame.K_DOWN]:
        y += vel
        left = False
        right = False
        up = False
        down = True
    else:
        walk = 0
    gameWindow()
    
pygame.quit()
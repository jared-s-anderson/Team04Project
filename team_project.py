import pygame
#from pygame import sprite
from boss import Boss
from enemy import Enemy
from stats import Stats
from pygame.draw import rect
from character import Character
from randQuestion import question, checkSolution
from sound import sounds
from CHARACTER_VARIABLES import *
from GAME_VARIABLES import *
from gmaeData import level01
import math
import random
from pytmx.util_pygame import load_pygame
import pytmx
import os


pygame.init()
# Set the window
win = pygame.display.set_mode((X, Y))
# Set the window name
pygame.display.set_caption(gameName)
# Set the scene and its dimensions.
bg = pygame.transform.scale(pygame.image.load(defaultScene), (X, Y))

#Set sounds by scene
sounds(scene, volume)

# Red Character and Stats and Movement
red = Character(pygame.image.load('images/Red_sprite/red_right_1.png'),
                RED_WIDTH, RED_HEIGHT, RED_VELOCITY)
red.rect.update(200, 50, RED_WIDTH, RED_HEIGHT)

red_stats = Stats(red)
red.movement_setup("Red_sprite", "red")

# Hydra Character
hydra = Boss(pygame.image.load("images/Hydra_boss/Hydra_1.png"), 
                HYDRA_WIDTH, HYDRA_HEIGHT)
hydra.rect.update(200, 200, HYDRA_WIDTH, HYDRA_HEIGHT)
hydra_stats = Stats(hydra)
hydra.movement_setup("Hydra_boss", "Hydra")
hydra.special_move_setup("Hydra_boss/Roar", "Hydra_roar")
hydra.turn_setup("Hydra_boss/Turn", "Hydra_turn")

# Eye Character 
eye = Enemy(pygame.image.load("images/Flying_eye/eye1.png"), EYE_WIDTH, EYE_HEIGHT, EYE_VELOCITY)
eye_stats = Stats(eye)
eye.movement_setup("Flying_eye")
eye.rect.update(EYE_X, EYE_Y, EYE_WIDTH, EYE_HEIGHT)

# Goblin Character
goblin = Enemy(pygame.image.load("images/Goblin/goblin1.png"), GOBLIN_WIDTH, GOBLIN_HEIGHT, GOBLIN_VELOCITY)
goblin_stats= Stats(goblin)
goblin.movement_setup("Goblin")
goblin.rect.update(GOBLIN_X, GOBLIN_Y, GOBLIN_WIDTH, GOBLIN_HEIGHT)

# Mushroom Character
mushroom = Enemy(pygame.image.load("images/Mushroom/mushroom1.png"), MUSHROOM_WIDTH, MUSHROOM_HEIGHT, MUSHROOM_VELOCITY)
mushroom_stats = Stats(mushroom)
mushroom.movement_setup("Mushroom")
mushroom.rect.update(MUSHROOM_X, MUSHROOM_Y, MUSHROOM_WIDTH, MUSHROOM_HEIGHT)

# Skeleton Character
skeleton = Enemy(pygame.image.load("images/Skeleton/skeleton1.png"), SKELETON_WIDTH, SKELETON_HEIGHT, SKELETON_VELOCITY)
skeleton_stats = Stats(skeleton)
skeleton.movement_setup("Skeleton")
skeleton.rect.update(SKELETON_X, SKELETON_Y, SKELETON_WIDTH, SKELETON_HEIGHT)

sprite_group = pygame.sprite.Group(red, hydra, eye, goblin, mushroom, skeleton)
#####################################################
 
# create a font object.
# 1st parameter is the font file which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# basic font for user typed
base_font = pygame.font.Font(None, 32)

# create a text surface object,
# on which text is drawn.
curQuestion = question(level)
text = font.render(curQuestion[0], True, TEXT_COLOR, TEXT_BACKGROUND)
levelText = font.render(str(level), True, LEVEL_COLOR, LEVEL_BACKGROUND)

# Define the empty user text string for user input
user_text = ''

# create rectangle
input_rect = pygame.Rect(INPUT_X, INPUT_Y, INPUT_WIDTH, INPUT_HIGHT)

#####################################################
eye_stats.damage_left -= 10

i = 0
all_tiles = []
tmx_data = load_pygame("Cave.tmx")
props = tmx_data.get_tile_properties_by_layer(1)
boundry_rects = []
for tile in tmx_data.get_layer_by_name("Tile Layer 1").tiles():
        x_pixel = tile[0] * 6
        y_pixel = tile[1] * 6   
        curr_rect = pygame.Rect(x_pixel, y_pixel, 12, 12) 
        boundry_rects.append(curr_rect)      

# set up the boundries:
left = []
right = []
top = []
down = []  

# for r in boundry_rects:
#     left.append(r.right)
#     right.append(r.left)
#     top.append(r.bottom)
#     down.append(r.top)
   
# Set up the game window
def gameWindow():
    global i
    if i >= 38:
        i = 0
    win.fill((0,0,0))
    for tile in tmx_data.get_layer_by_name("Tile Layer 1").tiles():
        x_pixel = tile[0] * 6
        y_pixel = tile[1] * 6   
        win.blit(tile[2], (x_pixel, y_pixel))
    for tile in tmx_data.get_layer_by_name("Tile Layer 2").tiles():
        x_pixel = tile[0] * 6
        y_pixel = tile[1] * 6   
        win.blit(tile[2], (x_pixel, y_pixel))


    sprite_group.draw(win)
    red_stats.show_health_bar(win, red.rect.x, red.rect.y)   
    hydra.showCharacter(win, i)
    hydra_stats.show_health_bar(win, hydra.rect.x + 35, hydra.rect.y)
    
    eye_stats.show_health_bar(win, eye.rect.x + 5, eye.rect.y)
    goblin_stats.show_health_bar(win, goblin.rect.x  + 5, goblin.rect.y)
    mushroom_stats.show_health_bar(win, mushroom.rect.x + 5, mushroom.rect.y)
    skeleton_stats.show_health_bar(win, skeleton.rect.x + 15, skeleton.rect.y)

    i += 1

def interface(win, rect, text, levelText, input_rect, user_text, color, base_font):

   # copying the text surface object to the display surface object 
    # at the center coordinate.
    textRect = text.get_rect()

    # draw rectangle and argument passed which should
    # be on screen
    rect(win, color, input_rect)

    # set the center of the text rectangle object.
    textRect.center = (TEXT_X, TEXT_Y)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    win.blit(levelText, (LEVEL_X, LEVEL_Y))
    win.blit(text, textRect)

    # set width of textfield so that text cannot get outside of user's text input
    # Origionally set to 100? Why does this exist?
    input_rect.w = max(INPUT_WIDTH, text_surface.get_width()+10)

    # The one and true update
    pygame.display.update()

run = True
which_color = 0

# This loop runs the game.
while run:
    pygame.time.delay(100)

    # Get the key pressed from user
    key = pygame.key.get_pressed()

    # Quit and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key [pygame.K_ESCAPE]:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                which_color = 1
            else:
                which_color = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(user_text)>0:
                     if len(user_text)>0:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                #output = 'Incorrect:'
                result = checkSolution(user_text, curQuestion[1], cheatAns)
                if result:
                    # If correct reset the color, increase the level, 
                    # and rerender the level image.
                    which_color = 1
                    level += 1
                    levelText = font.render(str(level), True, LEVEL_COLOR, LEVEL_BACKGROUND)
                else:
                    which_color = 2
                #print('{} Your level is: {}'.format(output, level))
                user_text = ''
                curQuestion = question(level)
                text = font.render(curQuestion[0], True, TEXT_COLOR, TEXT_BACKGROUND)
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
      
        if which_color == 0:
            color = pygame.Color(INPUT_COLOR_PASSIVE)
        elif which_color == 1:
            color = pygame.Color(INPUT_COLOR_ACTIVE)
        elif which_color == 2:
            color = pygame.Color(INPUT_COLOR_WRONG)
        else:
            print('which_color is invalid!')
    ######################################################
    # Update Character by sending a bunch of key button states as bools
 
    # Red
    red.update(key, hydra, boundry_rects)
            
    eye.update(red)
    goblin.update(red)
    mushroom.update(red)
    skeleton.update(red)
    hydra.update(red)
    red.draw()

    # Enemy movement
    eye.update(red, EYE_SIGHT)
    goblin.update(red, GOBLIN_SIGHT)
    mushroom.update(red, MUSHROOM_SIGHT)
    skeleton.update(red, SKELETON_SIGHT)
    hydra.update(red)
    

    # Eye

    # try to get enemy to chase player

    eye.draw()

    # Goblin
    goblin.draw()

    # Mushroom
    mushroom.draw()

    # Skeleton
    skeleton.draw()

    # call the game window elements
    gameWindow()
    interface(win, rect, text, levelText, input_rect, user_text, color, base_font)

print('Thanks for playing!')    
pygame.quit()
import pygame
from pygame import sprite
from boss import Boss
from enemy import Enemy
from object_finder import ObjectFinder
from stats import Stats
from pygame.draw import rect
from character import Character
from randQuestion import question, checkSolution
from sound import sounds
from CHARACTER_VARIABLES import *
from GAME_VARIABLES import *

pygame.init()

win = pygame.display.set_mode((X, Y)) 
bg = pygame.image.load('images/Tiles/map(9x6).png')
bg = pygame.transform.scale(bg, (X, Y))
pygame.display.set_caption(gameName)

#Set sounds by scene
sounds(scene, volume)

# Red Character and Stats and Movement
red = Character(pygame.image.load('images/Red_sprite/red_right_1.png'),
                RED_WIDTH, RED_HEIGHT, RED_VELOCITY)
red_stats = Stats(red)
red.movement_setup("Red_sprite", "red")

# Hydra Character
hydra = Boss(pygame.image.load("images/Hydra_boss/Hydra_1.png"), 
                HYDRA_WIDTH, HYDRA_HEIGHT)
hydra.rect.update(200, 50, HYDRA_WIDTH, HYDRA_HEIGHT)
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
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
question = question(level)
text = font.render(question[0], True, TEXT_BLOOD, TEXT_GREY)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the text rectangle object.
textRect.center = (TEXT_X, TEXT_Y)

###############################################

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''

# create rectangle
input_rect = pygame.Rect(INPUT_X, INPUT_Y, INPUT_WIDTH, INPUT_HIGHT)
  
# color_active stores color which switches
# to active when input box is clicked by user
color_active = pygame.Color(INPUT_COLOR_ACTIVE)
  
# color_passive stores the default color which is
# color of input box.
color_passive = pygame.Color(INPUT_COLOR_PASSIVE)
color = color_passive

#####################################################

i = 0



# Set up the game window
def gameWindow():
    
    global i
    
    if i >= 38:
        i = 0

    win.fill((0, 0, 0))
    win.blit(bg, (0,0))
    
    red_stats.show_health_bar(win, red.rect.x, red.rect.y)   
    sprite_group.draw(win)
    hydra.showCharacter(win, i)
    hydra_stats.show_health_bar(win, hydra.rect.x + 35, hydra.rect.y)
    eye_stats.show_health_bar(win, eye.rect.x + 5, eye.rect.y)
    goblin_stats.show_health_bar(win, goblin.rect.x  + 5, goblin.rect.y)
    mushroom_stats.show_health_bar(win, mushroom.rect.x + 5, mushroom.rect.y)
    skeleton_stats.show_health_bar(win, skeleton.rect.x + 15, skeleton.rect.y)

    i += 1
###################### Interface ##################################
    # copying the text surface object to the display surface object 
    # at the center coordinate.
    win.blit(text, textRect)
  
    # draw rectangle and argument passed which should
    # be on screen
    rect(win, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get outside of user's text input
    # Origionally set to 100? Why does this exist?
    input_rect.w = max(INPUT_WIDTH, text_surface.get_width()+10)

    # The one and true update
    pygame.display.update()

run = True
active = False

# This loop runs the game.
while run:
    pygame.time.delay(100)

    # Get the key pressed from user
    key = pygame.key.get_pressed()

    # Quit and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key [pygame.K_ESCAPE]:
            run = False

    ######################################################
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                result = checkSolution(user_text, question[1], cheatAns)
                if result == 'Correct!':
                    level += 1
                print(result + ' your level is: {}'.format(level))
                user_text = ''
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
      
        if active:
            color = color_active
        else:
            color = color_passive
    ######################################################
    # Update Character by sending a bunch of key button states as bools
 
    # Red
    red.update(key, hydra)
    red.draw()

    # Eye
    eye.draw()

    # Goblin
    goblin.draw()

    # Mushroom
    mushroom.draw()

    # Skeleton
    skeleton.draw()

    # call the game window elements
    gameWindow()
    
    
    

print('Thanks for playing!')    
pygame.quit()
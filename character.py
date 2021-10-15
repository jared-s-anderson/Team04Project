import pygame
from  CHARACTER_VARIABLES import *

class Character:

    def __init__(self, picture, w, h, v, x, y):

        # Character attributes
        self.character_name = ""
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.velocity = v
        self.abilities = []
    
        # Animation attributes
        self.standing = picture
        self.move_right = []
        self.move_left = [] 
        self.move_up = []
        self.move_down = []

        # input key values
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk = 0

    def movement_setup(self, folder_name, character_name):
        '''
        folder_name : name of the folder for the character with all of the animation images
            
             folder files should be formatted correctly:
                - {character_name}_{movement}_{movement_number}.png
                    - ex. red_right_1.png
                          /    |     \
            character_name movement number
        '''
        self.character_name = character_name
        self.move_right = [pygame.image.load(f"{folder_name}/{character_name}_right_{1}.png"), 
                            pygame.image.load(f'{folder_name}/{character_name}_right_{2}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_right_{3}.png')]

        self.move_left = [pygame.image.load(f'{folder_name}/{character_name}_left_{1}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_left_{2}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_left_{3}.png')]

        self.move_up = [pygame.image.load(f'{folder_name}/{character_name}_up_{1}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_up_{2}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_up_{3}.png')]

        self.move_down = [pygame.image.load(f'{folder_name}/{character_name}_down_{1}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_down_{2}.png'), 
                            pygame.image.load(f'{folder_name}/{character_name}_down_{3}.png')]

    def move(self, key):
        '''
        method that has the character move according to the {key} that was pressed

        '''
        if key[pygame.K_LEFT]:
            self.x -= self.velocity
            self.left = True
            self.right = False
            self.up = False
            self.down = False

        elif key[pygame.K_RIGHT]:
            self.x += self.velocity
            self.left = False
            self.right = True
            self.up = False
            self.down = False

        elif key[pygame.K_UP]:
            self.y -= self.velocity
            self.left = False
            self.right = False
            self.up = True
            self.down = False

        elif key[pygame.K_DOWN]:
            self.y += self.velocity
            self.left = False
            self.right = False
            self.up = False
            self.down = True

        else:
            self.walk = 0

    def showCharacter(self, win):
        '''
        Displays the character on the screen
        '''
        if self.walk + 1 >= 12:
            self.walk = 0
        if self.right:
            win.blit(self.move_right[self.walk // 4], (self.x, self.y))
            self.walk += 1
        elif self.left:
            win.blit(self.move_left[self.walk // 4], (self.x, self.y))
            self.walk += 1
        elif self.up:
            win.blit(self.move_up[self.walk // 4], (self.x, self.y))
            self.walk += 1
        elif self.down:
            win.blit(self.move_down[self.walk // 4], (self.x, self.y))
            self.walk += 1
        else:
            win.blit(self.standing, (self.x, self.y))
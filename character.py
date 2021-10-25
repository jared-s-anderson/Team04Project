import pygame
from  CHARACTER_VARIABLES import *
import os

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

        # Get all the files in the {folder}
        files_list = os.listdir(f"images/{folder_name}")
       
        for file in files_list:
            if "right" in file:
                self.move_right.append(pygame.image.load(f"images/{folder_name}/{file}"))
            elif "left" in file:
                self.move_left.append(pygame.image.load(f"images/{folder_name}/{file}"))
            elif "up" in file:
                self.move_up.append(pygame.image.load(f"images/{folder_name}/{file}"))
            elif "down" in file:
                self.move_down.append(pygame.image.load(f"images/{folder_name}/{file}"))

    def move(self, key):
        '''
        method that has the character move according to the {key} that was pressed

        '''
        if key[pygame.K_LEFT] and self.x > self.velocity:
            self.x -= self.velocity
            self.left = True
            self.right = False
            self.up = False
            self.down = False

        elif key[pygame.K_RIGHT] and self.x  < 1315 - self.width - self.velocity:
            self.x += self.velocity
            self.left = False
            self.right = True
            self.up = False
            self.down = False

        elif key[pygame.K_UP] and self.y > self.velocity:
            self.y -= self.velocity
            self.left = False
            self.right = False
            self.up = True
            self.down = False

        elif key[pygame.K_DOWN] and self.y < 675 - self.width - self.velocity:
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
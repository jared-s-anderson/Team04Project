#from typing import Tuple
import pygame
from  CHARACTER_VARIABLES import *
import os
from OBJECT_VARIABLES import *
import object_finder

class Character(pygame.sprite.Sprite):
    def __init__(self, picture, w, h, v):
        super().__init__()

        self.image = picture.convert_alpha()
        self.rect = self.image.get_rect()
        self.index = 0
        
        # Character attributes
        self.character_name = ""
        self.width = w
        self.height = h
        self.velocity = v
        self.abilities = []
        self.damage_left = 50
    
        # Animation attributes
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
                self.move_right.append(pygame.image.load(f"images/{folder_name}/{file}").convert_alpha())
            elif "left" in file:
                self.move_left.append(pygame.image.load(f"images/{folder_name}/{file}").convert_alpha())
            elif "up" in file:
                self.move_up.append(pygame.image.load(f"images/{folder_name}/{file}").convert_alpha())
            elif "down" in file:
                self.move_down.append(pygame.image.load(f"images/{folder_name}/{file}").convert_alpha())

    def update(self, key, other, b_list):
        '''
        method that has the character move according to the {key} that was pressed

        '''
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        if key[pygame.K_LEFT] and (self.rect.x > self.velocity): 
            # Set animation 
            self.left = True
            # Check boundry collision 
            if self.rect.collidelist(b_list) != -1:
                # Let character move back right into the map, away from boundry
                self.rect = self.rect.move(self.velocity, 0)
                return
            # Move character left 
            self.rect = self.rect.move(-self.velocity, 0)

        elif key[pygame.K_RIGHT] and (self.rect.x  < 1315 - self.width - self.velocity):
            # Set animation
            self.right = True
            # Check boundry collision
            if self.rect.collidelist(b_list) != -1:
                # Let character move back left into the map, away from boundry
                self.rect = self.rect.move(-self.velocity, 0)
                return
            # Move character right
            self.rect = self.rect.move(self.velocity, 0)

        elif key[pygame.K_UP] and (self.rect.y > self.velocity):
            # Set animation
            self.up = True
            # Check boundry collision
            if self.rect.collidelist(b_list) != -1:
                # Let character move back down into the map, away from boundry
                self.rect = self.rect.move(0, self.velocity)
                return
            # Move character up
            self.rect = self.rect.move(0, -self.velocity)
            
        elif key[pygame.K_DOWN] and (self.rect.y < 675 - self.width - self.velocity):
            # Set animation
            self.down = True
            # Check boundry collision
            if self.rect.collidelist(b_list) != -1:
                # Let character move back up into the map, away from boundry
                self.rect = self.rect.move(0, -self.velocity)
                return
            # Move character down
            self.rect = self.rect.move(0, self.velocity)

    def draw(self):
        '''
        Displays the character on the screen
        '''
        if self.index >= len(self.move_right):
            self.index = 0
        if self.right:
            self.image = self.move_right[self.index].convert_alpha()
            self.index += 1
        elif self.left:
            self.image = self.move_left[self.index].convert_alpha()
            self.index += 1
        elif self.up:
            self.image = self.move_up[self.index].convert_alpha()
            self.index += 1
        elif self.down:
            self.image = self.move_down[self.index].convert_alpha()
            self.index += 1

    def show_health_bar(self, win, x, y):
        '''
        Displays the characters health bar
        
        '''
        if self.alive:
            GREEN_LEFT = 0
            TOP = 0
            WIDTH = 50
            HEIGHT = 8

            health_bar = pygame.Surface((WIDTH, HEIGHT))
            health_bar.fill(pygame.Color("green"), (GREEN_LEFT, TOP, WIDTH, HEIGHT))
            health_bar.fill(pygame.Color("red"), (self.damage_left, TOP, WIDTH, HEIGHT))

            win.blit(health_bar, (x - 10, y - 20))
        
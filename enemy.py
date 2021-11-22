import pygame
import os
from character import Character
import math

class Enemy(Character):
    def __init__(self, picture, w, h, v):
        super().__init__(picture, w, h, v)

        self.image_list = []
        #self.image = picture.convert()
        #self.rect = self.image.get_rect()
        #self.index = 0

    def follow_player(self, character):
        x, y = character.rect.x - self.rect.x, character.rect.x - self.rect.y
        distance = math.hypot(x, y)
        x, y = x  / distance, y / distance
        self.rect.x += x * self.velocity
        self.rect.y += y * self.velocity

    def follow_player2(self, character):
        dirvect = pygame.Math.Vector2(character.rect.x - self.rect.x, character.rect.y - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(self.velocity)
        self.rect.move_ip(dirvect)

    def movement_setup(self, folder_name):

        # self.enemy_name = enemy_name
        files_list = os.listdir(f"images/{folder_name}")
    
        for file in files_list:
            self.image_list.append(pygame.image.load(f"images/{folder_name}/{file}").convert_alpha())
        
        print(self.image_list)
        
    def draw(self):
        if self.index >= len(self.image_list):
            self.index = 0
        self.image = self.image_list[self.index].convert_alpha()
        self.index += 1

    def update(self,red):
        delta_x = red.rect.x - self.rect.x
        delta_y = red.rect.y - self.rect.y

        self.rect = self.rect.move(self.velocity + delta_x / 10, delta_y / 10)
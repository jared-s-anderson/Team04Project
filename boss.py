from character import Character
import pygame

class Boss(Character):
    
    def __init__(self, picture, w, h, x, y):
        super().__init__(picture, w, h, 0, x, y)

        # Unique Boss Animations
        self.rotate_right = []
        self.rotate_left = []
        self.rise = []
        self.special_attack_move = []
        self.standing_animation = []

    def movement_setup(self, folder_name, character_name):
        self.character_name = character_name

        for i in range(1, 12):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png"))
    
    def showCharacter(self, win, i):
        win.blit(self.standing_animation[i], (self.x, self.y))

    def special_move_setup(self, folder_name, character_name):
        for i in range(1, 5):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png"))
        for i in range(10):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{4}.png"))
        for i in range(4,0, -1):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png"))
    
    # def show_special_move(self, win, i):
    #     win.blit(self.standing_animation[i], (self.x, self.y))

from character import Character
import pygame

class Boss(Character):
    
    def __init__(self, picture, w, h,):
        super().__init__(picture, w, h, 0,)

        # Unique Boss Animations
        self.rotate_right = []
        self.rotate_left = []
        self.rise = []
        self.special_attack_move = []
        self.standing_animation = []

    def movement_setup(self, folder_name, character_name):
        self.character_name = character_name

        for i in range(1, 12):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png").convert_alpha())
    
    def showCharacter(self, win, i):
        self.image = self.standing_animation[i]

    def special_move_setup(self, folder_name, character_name):
        for i in range(1, 5):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png").convert_alpha())
        for i in range(5):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{4}.png").convert_alpha())
        for i in range(4,0, -1):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png").convert_alpha())
    
    # def show_special_move(self, win, i):
    #     win.blit(self.standing_animation[i], (self.x, self.y))

    def turn_setup(self, folder_name, character_name):
        for i in range(1, 3):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png").convert_alpha())
        for i in range(10):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{2}.png").convert_alpha())
        for i in range(2, 0, -1):
            self.standing_animation.append(pygame.image.load(f"images/{folder_name}/{character_name}_{i}.png").convert_alpha())

    def update(self,red):
        delta_x = red.rect.x - self.rect.x
        delta_y = red.rect.y - self.rect.y

        self.rect = self.rect.move(delta_x / 20, delta_y / 20)
from character import Character

class Boss(Character):
    
    def __init__(self, picture, w, h, x, y):
        super().__init__(picture, w, h, 0, x, y)

        # Unique Boss Animations
        self.rotate_right = []
        self.rotate_left = []
        self.rise = []
        self.special_attack_move = []

    def movement_setup(self, folder_name, character_name):
        #TODO: Add boss movement setup
        pass 
        
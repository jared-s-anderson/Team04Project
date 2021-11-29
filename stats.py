import pygame

class Stats:
    '''
    Class for character health, damage power, and special abilities
    
    '''

    def __init__(self, character):
        self.character = character
        self.health = 100
        self.damage_power = 0
        self.abilities = character.abilities
        self.damage_left = 50
        self.alive = True

    def set_health(self):
        '''
        Sets the initial amount of health the character has
        The initial amount of health is determined by the type of character (player, enemy, boss, ect..)

        '''
        pass

    def set_damage_power(self, weapon):
        '''
        Sets the amount of damage the character can deal.
        
        The initial damage power will be determined by the type of character (player, enemy, boss, ect..), their current weapon and abilities.

        weapon: the current weapon that the character is using. This helps determine how much damage 
                power the character will have. 
        '''
        pass



    def update_health(self, decrease):
        '''
        Updates the character's health. 
        
        This method is dependent upon three main things:
            - The health of the current Character.
            - The damage power of the one who blew the hit
            - The abilities of both parties 

        decrease (boolean): whether there will be a decrease in health (if the character just got hit by another)
                            - If True: health needs to be subtracted
                            - If False: the character will retrieve more health (because of healing ability, health kit, ect...)
        
        '''
        pass

    def update_damage_power(self):
        '''
        Updates the amount of damage the character can blow. 

        This method is mainly dependant on the type character (player, enemy, boss, ect..) and what
        special abilities they currently have in use. 


        '''
        pass

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

    def show_abilities(self):
        '''
        Displays the current abilites the character has. 
        Also in charge of showing which ability is currently in use, if any. 
        '''
        pass
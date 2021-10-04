class Stats:
    '''
    Class for character health, damage power, and special abilities
    
    '''

    def __init__(self, character):
        self.character = character
        self.health
        self.damage_power
        self.abilities

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

    def set_abilities(self, current_abilities):
        '''
        Sets the abilities of the character. Each ability gives the character certain upgrades and advantages. 
        
        Each character can have up to three abilities. 

        current_abilities: the character's current abilities. This is used to determine if the character is allowed
                            more abilities or if they will have to choose to replace one of them with a new ability. 
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

    def update_abilities(self, current_abilities, new_abilities, changes):
        '''
        Updates abilities of the character. Similiar to set_abilities.
        
        In charge of a few things:
            - Replacing current abilities with new ones. 
            - Upgrading abilities 
            - Modifying current abilities for specific battles

        current_abilities: all of the current character abilities that will need to be updated / replaced.
        new_abilities: the new abilities that will replace old_abilites
        changes: all of the updates to the current abilities
        '''
        pass

    def show_health_bar(self):
        '''
        Displays the characters health bar
        
        '''
        pass

    def show_abilities(self):
        '''
        Displays the current abilites the character has. 
        Also in charge of showing which ability is currently in use, if any. 
        '''
        pass
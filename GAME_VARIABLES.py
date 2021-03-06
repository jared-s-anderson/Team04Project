from pytmx.util_pygame import load_pygame
# General use variables
X = 1280 
Y = 650 #-AD 650 default 760
gameName = "The Legend of the Red Rectangle"
level = 1 # Here is the cheat to set your own level
cheatAns = 42 # This lets you set a cheat answer - can be disabled by setting to 0
damage_enemy = False

# Scene Set
scene = 'overworld'

# Sound settings
volume = 0.7

# Text
TEXT_X = X//2
TEXT_Y = Y//15
TEXT_COLOR = (150, 42, 35) # Blood red
TEXT_BACKGROUND = (31, 26, 26) # Grey

# Input box
INPUT_X = X//3
INPUT_Y = Y//1.2
INPUT_WIDTH = X//3 #140
INPUT_HIGHT = 32
INPUT_COLOR_ACTIVE =  (74, 70, 70) # Light grey
INPUT_COLOR_PASSIVE = (61, 58, 58) # Dark grey
INPUT_COLOR_WRONG = (181, 20, 5) # Bright red

# Level text
LEVEL_X = X//1.2
LEVEL_Y = Y//1.2
LEVEL_COLOR = (150, 42, 35) # Blood red
LEVEL_BACKGROUND = (31, 26, 26) # Grey
from GAME_VARIABLES import *
import pygame

# Set up the game window
def gameWindow(win, bg, red, red_stats, hydra, hydra_stats, sprite_group):
    i = 0

    if i >= 38:
        i = 0

    win.fill((0, 0, 0))
    win.blit(bg, (0,0))

    red_stats.show_health_bar(win, red.rect.x, red.rect.y)   
    sprite_group.draw(win)
    hydra.showCharacter(win, i)
    hydra_stats.show_health_bar(win, hydra.rect.x + 35, hydra.rect.y)

    i += 1

def interface(win, rect, text, levelText, input_rect, user_text, color, base_font):

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the text rectangle object.
    textRect.center = (TEXT_X, TEXT_Y)

    # copying the text surface object to the display surface object 
    # at the center coordinate.
    win.blit(levelText, (LEVEL_X, LEVEL_Y))
    win.blit(text, textRect)
    
    # draw rectangle and argument passed which should
    # be on screen
    rect(win, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get outside of user's text input
    # Origionally set to 100? Why does this exist?
    input_rect.w = max(INPUT_WIDTH, text_surface.get_width()+10)

    # The one and true update
    pygame.display.update()
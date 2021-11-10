from GAME_VARIABLES import *
import pygame

def interface(win, rect, text, levelText, input_rect, user_text, color, base_font):

   # copying the text surface object to the display surface object 
    # at the center coordinate.
    textRect = text.get_rect()

    # draw rectangle and argument passed which should
    # be on screen
    rect(win, color, input_rect)

    # set the center of the text rectangle object.
    textRect.center = (TEXT_X, TEXT_Y)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    win.blit(levelText, (LEVEL_X, LEVEL_Y))
    win.blit(text, textRect)

    # set width of textfield so that text cannot get outside of user's text input
    # Origionally set to 100? Why does this exist?
    input_rect.w = max(INPUT_WIDTH, text_surface.get_width()+10)

    # The one and true update
    pygame.display.update()
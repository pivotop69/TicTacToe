import pygame
import sys
from settings1 import Settings
import gamefunctions as gf
from play_again import Play
from whowon import Won
def run_game():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    circles_won = Won(setting, screen, "Circles - Won!")
    cross_won = Won(setting, screen, "Cross' - Won!")
    tie = Won(setting, screen, "Tie!")
    play = Play(setting, screen, "Play Again", )
    pygame.display.set_caption(setting.caption)
    screen.fill(setting.bg_color)
    gf.screen_cross(screen)
    run = True
    while run:
        result = gf.return_circles(setting)
        result1 = gf.return_cross(setting)
        if result in setting.penis:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play.draw_button()
            circles_won.draw_text()
            gf.check_button(play, screen, setting, mouse_x, mouse_y) 
        elif result1 in setting.penis:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play.draw_button()
            cross_won.draw_text()
            gf.check_button(play, screen, setting, mouse_x, mouse_y)
        elif len(setting.circle_list) == 5:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play.draw_button()
            tie.draw_text()
            gf.check_button(play, screen, setting, mouse_x, mouse_y)              
        gf.check_events(setting, screen)
run_game()
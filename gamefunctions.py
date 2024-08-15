import pygame
import sys
from settings1 import Settings
def check_events(setting, screen):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
               
                if mouse_x in range(setting.rect_1_x[0], setting.rect_1_x[1]) and mouse_y in range(setting.rect_1_y[0], setting.rect_1_y[1]) and 1 not in setting.circle_list and 1 not in setting.crosshair_list:
                    if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_1_x[1] - 166
                        y = setting.rect_1_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(1)
                    elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_1_x[0] + 50; y = setting.rect_1_y[0] + 50
                        x2 = setting.rect_1_x[1] - 50; y2 = setting.rect_1_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_1_x[1] - 50; y = y 
                        x2 = setting.rect_1_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(1)
               
                elif mouse_x in range(setting.rect_2_x[0], setting.rect_2_x[1]) and mouse_y in range(setting.rect_2_y[0], setting.rect_2_y[1]) and 2 not in setting.circle_list and 2 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_2_x[1] - 166
                        y = setting.rect_2_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(2)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_2_x[0] + 50; y = setting.rect_2_y[0] + 50
                        x2 = setting.rect_2_x[1] - 50; y2 = setting.rect_2_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_2_x[1] - 50; y = y 
                        x2 = setting.rect_2_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(2)
               
                elif mouse_x in range(setting.rect_3_x[0], setting.rect_3_x[1]) and mouse_y in range(setting.rect_3_y[0], setting.rect_3_y[1]) and 3 not in setting.circle_list and 3 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_3_x[1] - 166
                        y = setting.rect_3_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(3)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_3_x[0] + 50; y = setting.rect_3_y[0] + 50
                        x2 = setting.rect_3_x[1] - 50; y2 = setting.rect_3_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_3_x[1] - 50; y = y 
                        x2 = setting.rect_3_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(3)
               
                elif mouse_x in range(setting.rect_4_x[0], setting.rect_4_x[1]) and mouse_y in range(setting.rect_4_y[0], setting.rect_4_y[1]) and 4 not in setting.circle_list and 4 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_4_x[1] - 166
                        y = setting.rect_4_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(4)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_4_x[0] + 50; y = setting.rect_4_y[0] + 50
                        x2 = setting.rect_4_x[1] - 50; y2 = setting.rect_4_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_4_x[1] - 50; y = y 
                        x2 = setting.rect_4_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(4)
                
                elif mouse_x in range(setting.rect_5_x[0], setting.rect_5_x[1]) and mouse_y in range(setting.rect_5_y[0], setting.rect_5_y[1]) and 5 not in setting.circle_list and 5 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_5_x[1] - 166
                        y = setting.rect_5_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(5)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_5_x[0] + 50; y = setting.rect_5_y[0] + 50
                        x2 = setting.rect_5_x[1] - 50; y2 = setting.rect_5_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_5_x[1] - 50; y = y 
                        x2 = setting.rect_5_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(5)
                
                elif mouse_x in range(setting.rect_6_x[0], setting.rect_6_x[1]) and mouse_y in range(setting.rect_6_y[0], setting.rect_6_y[1]) and 6 not in setting.circle_list and 6 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_6_x[1] - 166
                        y = setting.rect_6_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(6)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_6_x[0] + 50; y = setting.rect_6_y[0] + 50
                        x2 = setting.rect_6_x[1] - 50; y2 = setting.rect_6_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_6_x[1] - 50; y = y 
                        x2 = setting.rect_6_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(6)
                
                elif mouse_x in range(setting.rect_7_x[0], setting.rect_7_x[1]) and mouse_y in range(setting.rect_7_y[0], setting.rect_7_y[1]) and 7 not in setting.circle_list and 7 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_7_x[1] - 166
                        y = setting.rect_7_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(7)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_7_x[0] + 50; y = setting.rect_7_y[0] + 50
                        x2 = setting.rect_7_x[1] - 50; y2 = setting.rect_7_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_7_x[1] - 50; y = y 
                        x2 = setting.rect_7_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(7)
                
                elif mouse_x in range(setting.rect_8_x[0], setting.rect_8_x[1]) and mouse_y in range(setting.rect_8_y[0], setting.rect_8_y[1]) and 8 not in setting.circle_list and 8 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_8_x[1] - 166
                        y = setting.rect_8_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(8)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_8_x[0] + 50; y = setting.rect_8_y[0] + 50
                        x2 = setting.rect_8_x[1] - 50; y2 = setting.rect_8_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_8_x[1] - 50; y = y 
                        x2 = setting.rect_8_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(8)
                
                elif mouse_x in range(setting.rect_9_x[0], setting.rect_9_x[1]) and mouse_y in range(setting.rect_9_y[0], setting.rect_9_y[1]) and 9 not in setting.circle_list and 9 not in setting.crosshair_list:
                     if len(setting.circle_list) <= len(setting.crosshair_list):   
                        x = setting.rect_9_x[1] - 166
                        y = setting.rect_9_y[1] - 166
                        draw_circle(screen, x, y)
                        setting.circle_list.append(9)
                     elif len(setting.circle_list) > len(setting.crosshair_list):
                        x = setting.rect_9_x[0] + 50; y = setting.rect_9_y[0] + 50
                        x2 = setting.rect_9_x[1] - 50; y2 = setting.rect_9_y[1] - 50
                        draw_crosshair(screen, x, y, x2, y2)
                        x = setting.rect_9_x[1] - 50; y = y 
                        x2 = setting.rect_9_x[0] + 50; y2 = y2
                        draw_crosshair(screen, x, y, x2, y2)
                        setting.crosshair_list.append(9)            
    pygame.display.flip()

def screen_cross(screen):
     pygame.draw.line(screen, (0, 0, 0), (333, 0), (333, 999), 5)
     pygame.draw.line(screen, (0, 0, 0), (666, 0), (666, 999), 5)
     pygame.draw.line(screen, (0, 0, 0), (0, 333), (999, 333), 5)
     pygame.draw.line(screen, (0, 0, 0), (0, 666), (999, 666), 5)

def draw_circle(screen, x, y):
     pygame.draw.circle(screen, (0, 0, 0), (x, y), 100, 5)

def draw_crosshair(screen, x, y, x2, y2):
     pygame.draw.line(screen, (0, 0, 0), (x, y), (x2, y2), 8)

def check_button(play, screen, setting, mouse_x, mouse_y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_cliked = play.rect.collidepoint(mouse_x, mouse_y)
    for event in pygame.event.get():    
        if button_cliked:
            if event.type == pygame.MOUSEBUTTONDOWN:    
                restart_game(screen, setting)

def restart_game(screen, setting):
    screen.fill(setting.bg_color)
    setting.circle_list = []
    setting.crosshair_list = []
    screen_cross(screen)
    check_events(setting, screen)

def return_circles(setting):     
            if len(setting.circle_list) >= 3:
                for elem in setting.penis:
                    lst = []               
                    for i in elem:
                        if i in setting.circle_list and i not in lst:
                            lst.append(i)               
                    if lst == elem:
                        return lst

def return_cross(setting):     
    if len(setting.crosshair_list) >= 3:
        for elem in setting.penis:
            lst2 = []                
            for i in elem:
                if i in setting.crosshair_list and i not in lst2:
                    lst2.append(i)               
            if lst2 == elem:
                return lst2

                

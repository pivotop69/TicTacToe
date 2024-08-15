import pygame.font
class Won():

    def __init__(self, setting, screen, text):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 255, 0)
        self.bg_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.text_(self, text)
        
    def text_(self, setting, text):
        self.image = self.font.render(text, True, self.text_color, self.bg_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = 500
        self.image_rect.top = self.image_rect.top + 20
    
    def draw_text(self):
        self.screen.blit(self.image, self.image_rect)
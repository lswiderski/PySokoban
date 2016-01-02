__author__ = 'neufrin'
import pygame



menu_font = pygame.font.Font(None, 40)
class Label:

    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
    def draw(self,screen):
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True,(255, 255, 255))

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def set_text(self,text):
        self.text = text
        self.set_rect()

__author__ = 'neufrin'
import pygame
import Helper
pygame.font.init()
menu_font = pygame.font.Font(None, 40)
class Option:

    hovered = False

    def __init__(self, text, pos,action):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.action = action

    def draw(self,screen):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (50, 50, 50)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def doAction(self):
        Helper.actualscreen = self.action

__author__ = 'neufrin'
import pygame
import Screen
import Option
import Helper
import os

logo = pygame.image.load('Content/logo.png')

class MainMenu(Screen.Screen):
    def __init__(self):
        super(MainMenu, self,).__init__("mainmenu")
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.image.load(os.path.join('Content', 'logo.png'))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x =150
        self.sprite.rect.y =100
        self.logogroup = pygame.sprite.Group()
        self.logogroup.add(self.sprite)
        self.options = [Option.Option("PLAY", (100, 400),"selectlevel"),
           Option.Option("CREDITS", (100, 450),"credits")]


    def update(self,events):
        crashed = False
        for option in self.options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
        for event in events:
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for option in self.options:
                    if option.hovered == True:
                        option.doAction()
        return crashed

    def draw(self,screen):
        for option in self.options:
            option.draw(screen)
        self.logogroup.draw(screen)

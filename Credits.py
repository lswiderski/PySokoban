__author__ = 'neufrin'
import pygame
import Screen
import Option
import Label

class Credits(Screen.Screen):
    def __init__(self):
        super(Credits, self,).__init__("credits")
        self.options = [Option.Option("Back", (140, 105),"mainmenu")]
        self.labels = [Label.Label("Made by Lukasz Swiderski", (140, 145))]


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
            print(event)
        return crashed

    def draw(self,screen):
        for option in self.options:
            option.draw(screen)
        for label in self.labels:
            label.draw(screen)


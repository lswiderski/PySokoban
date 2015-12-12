__author__ = 'neufrin'
__author__ = 'neufrin'
import pygame
import Screen
import Option
import Label

class FinishedLevel(Screen.Screen):
    def __init__(self):
        super(FinishedLevel, self,).__init__("finishedlevel")
        self.options = [Option.Option("Back to Menu", (140, 105),"mainmenu"), Option.Option("Next level", (140, 145),"level")]
        self.labels = [Label.Label("Label", (140, 345))]


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


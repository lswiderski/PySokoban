__author__ = 'neufrin'
__author__ = 'neufrin'
import pygame
import Screen
import Option
import Label
import Helper

class FinishedLevel(Screen.Screen):
    def __init__(self):
        super(FinishedLevel, self,).__init__("finishedlevel")
        self.options = [Option.Option("Back to Menu", (100, 500),"mainmenu"), Option.Option("Next level", (550, 500),"level")]
        self.labels = [Label.Label("Congratulations you finished level", (160, 205)), Label.Label(Helper.TIME_IN_LAST_LEVEL, (330, 300)), Label.Label("Moves: %d" %Helper.MOVES_IN_LAST_LEVEL, (345, 350)) ]


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

        self.labels[1].set_text(Helper.TIME_IN_LAST_LEVEL)
        self.labels[2].set_text("Moves: %d" %Helper.MOVES_IN_LAST_LEVEL)
        return crashed

    def draw(self,screen):
        for option in self.options:
            option.draw(screen)
        for label in self.labels:
            label.draw(screen)


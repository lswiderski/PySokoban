__author__ = 'neufrin'
__author__ = 'neufrin'
import pygame
import Screen
import Option
import Label
import Helper
class SelectLevel(Screen.Screen):
    def __init__(self):
        super(SelectLevel, self,).__init__("selectlevel")
        self.options = [Option.Option("Back", (140, 105),"mainmenu"),]
        self.labels = [Label.Label("Label", (140, 345))]
        self.levels = []
        row =105
        for level in Helper.levels:
            self.levels.append(Option.Option(level, (400, row),level))
            row+=40


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


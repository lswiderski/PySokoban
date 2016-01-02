__author__ = 'neufrin'
import pygame
import Helper

sheet = pygame.image.load('Content/clock.png')

class Clock(pygame.sprite.Sprite):

    def __init__(self):
        super(Clock, self).__init__()
        self.slower = 0
        self.image = pygame.Surface([Helper.SCREEN_WIDTH, Helper.SCREEN_HEIGHT])
        self.setFrame(0)
        self.rect = self.image.get_rect()
        self.rect.x = Helper.SCREEN_WIDTH-32-5
        self.rect.y = 5
        self.actualFrame = 0

    def setFrame(self,number):
        sheet.set_clip(pygame.Rect(number*32,0,32,32))
        self.image =  sheet.subsurface(sheet.get_clip())
        return self.image

    def update(self):
        self.slower+=1
        if self.slower>15:
            if self.actualFrame < 3:
                self.actualFrame+=1
            else:
                self.actualFrame=0
            self.setFrame(self.actualFrame)
            self.slower=0

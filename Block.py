__author__ = 'neufrin'
import pygame


SPRT_WIDTH = 64
SPRT_HEIGHT = 64
sheet = pygame.image.load('sb_texture.png')


class Block(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super(Block, self).__init__()
        self.image = pygame.Surface([SPRT_WIDTH, SPRT_HEIGHT])

        if(type == " " ):# "Floor"
            sheet.set_clip(pygame.Rect(5*SPRT_WIDTH,0,SPRT_WIDTH,SPRT_HEIGHT))
        elif(type == "#"): # "Wall"
            sheet.set_clip(pygame.Rect(4*SPRT_WIDTH,0,SPRT_WIDTH,SPRT_HEIGHT))
        elif(type == "*"): # "Goal"
            sheet.set_clip(pygame.Rect(2*SPRT_WIDTH,0,SPRT_WIDTH,SPRT_HEIGHT))
        elif(type == "."): # "Empty"
            sheet.set_clip(pygame.Rect(3*SPRT_WIDTH,0, SPRT_WIDTH,SPRT_HEIGHT))
        elif(type == "$"): # "Box"
            sheet.set_clip(pygame.Rect(1*SPRT_WIDTH,0, SPRT_WIDTH,SPRT_HEIGHT))
        elif(type == "@"): # "Player"
            sheet.set_clip(pygame.Rect(0*SPRT_WIDTH,0, SPRT_WIDTH,SPRT_HEIGHT))

        self.image = sheet.subsurface(sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x*SPRT_WIDTH
        self.rect.y = y*SPRT_HEIGHT
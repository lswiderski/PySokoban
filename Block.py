__author__ = 'neufrin'
import pygame


SPRT_WIDTH = 64
SPRT_HEIGHT = 64
SCALE = 0.5
sheet = pygame.image.load('sb_texture.png')


class Block(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super(Block, self).__init__()
        self.image = pygame.Surface([SPRT_WIDTH, SPRT_HEIGHT])
        self.setSprite(type)
        self.rect = self.image.get_rect()
        self.rect.x = x*SPRT_WIDTH*SCALE
        self.rect.y = y*SPRT_HEIGHT*SCALE
        self.type = type
        self.x = x
        self.y = y

    def setSprite(self,type):
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

        self.image =  sheet.subsurface(sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (int(SPRT_WIDTH*SCALE), int(SPRT_HEIGHT*SCALE)))
        return self.image

    def changePositin(self,x,y):
        self.x=x
        self.y=y
        self.rect.x = x*SPRT_WIDTH*SCALE
        self.rect.y = y*SPRT_HEIGHT*SCALE

    def moveUp(self):
        self.changePositin(self.x,self.y-1)

    def moveDown(self):
        self.changePositin(self.x,self.y+1)

    def moveLeft(self):
        self.changePositin(self.x-1,self.y)

    def moveRight(self):
        self.changePositin(self.x+1,self.y)
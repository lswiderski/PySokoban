__author__ = 'neufrin'
import pygame
import Map

MapFile = ["#####", "#@  #", "# $.#", "# $.#", "#####"]
MapFile2 = ["  ####", "### @#","#    #","# .#.###","# $    #","##*#*# #","# $    #","#   ####", "#####"]

class Level:
    def __init__(self):
        self.player = pygame.sprite.Group()
        self.box_list = pygame.sprite.Group()
        self.load(MapFile2)

    def load(self, mapFile):
        self.map = Map.Map("1",mapFile)
        self.map.build(self)

    def draw(self,screen):
        self.map.draw(screen)
        self.box_list.draw(screen)
        self.player.draw(screen)

    def addPlayer(self,_player):
        self.player.add(_player)

    def addBox(self,_box):
        self.box_list.add(_box)

    def playerMoveUp(self):
        p = self.player.sprites()[0]
        if(self.isWallOnPlace( p.x, p.y-1)==False):
            p.moveUp()
    def playerMoveDown(self):
        p = self.player.sprites()[0]
        if(self.isWallOnPlace( p.x, p.y+1)==False):
            p.moveDown()
    def playerMoveLeft(self):
        p = self.player.sprites()[0]
        if(self.isWallOnPlace( p.x-1, p.y)==False):
            p.moveLeft()
    def playerMoveRight(self):
        p = self.player.sprites()[0]
        if(self.isWallOnPlace( p.x+1, p.y)==False):
            p.moveRight()

    def isBoxOnPlace(self, x, y):
        for i in self.box_list.sprites():
            if( i.x==x and i.y==y):
                if(i.type=="$" or i.type=="*"):
                    return True
        return False

    def isWallOnPlace(self, x, y):
        for i in self.map.bl_list.sprites():
            if( i.x==x and i.y==y):
                if(i.type=="#"):
                    return True
        return False




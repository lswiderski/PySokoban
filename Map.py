__author__ = 'neufrin'
import pygame
import Block
import Box
import Player
import MapLoader

class Map:
    def  __init__(self, name, mapname):
        self.Name = name
        self.mapfile = mapname
        self.mLoader = MapLoader.MapLoader(mapname)
        self.mapstring =  self.mLoader.map
        self.bl_list = pygame.sprite.Group()

    def build(self,level):
        self.level = level
        for (i,row) in enumerate(self.mapstring):
            for (j,type) in enumerate(row):
                print  i,j,type
                self.bl_list.add(self.makeBlock(type,j,i))

    def makeBlock(self,type,x,y):
        if(type == " " ):# "Floor"
           block = Block.Block(type, x, y)
        elif(type == "#"): # "Wall"
            block = Block.Block(type, x, y)
        elif(type == "*"): # "Goal"
            block = self.makeBlock(".",x,y) #make Empty
            self.level.addBox(Box.Box(x,y,type))
        elif(type == "."): # "Empty"
             block = Block.Block(type, x, y)
        elif(type == "$"): # "Box"
            block = self.makeBlock(" ",x,y) #make floor
            self.level.addBox(Box.Box(x,y,type))
        elif(type == "@"): # "Player"
            block =  self.makeBlock(" ",x,y)#make floor
            self.level.addPlayer(Player.Player(x,y))
        elif(type == "+"): # "Player on goal place"
            block =  self.makeBlock(".",x,y)#make empty
            self.level.addPlayer(Player.Player(x,y))
        return block

    def draw(self, screen):
        self.bl_list.draw(screen)

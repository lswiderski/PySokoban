__author__ = 'neufrin'
import pygame
import Block
import Box
import Player
import Helper

class Map:
    def  __init__(self, name, mapstring):
        self.Name = name
        self.mapstring = mapstring
        self.bl_list = pygame.sprite.Group()

    def build(self,level):
        self.level = level
        self.bl_list.empty()
        self.level.player.empty()
        self.level.box_list.empty()
        tmp = len(self.mapstring)
        if tmp>8:
            Helper.SCALE = 0.5
        else:
            Helper.SCALE = 1
        Helper.OFFSET_X = Helper.SCREEN_WIDTH/2 -((Helper.SPRT_WIDTH*Helper.SCALE*tmp)/2)
        Helper.OFFSET_Y = Helper.SCREEN_HEIGHT/2 -((Helper.SPRT_HEIGHT*Helper.SCALE*tmp)/2)
        for (i,row) in enumerate(self.mapstring):
            lastType =" ";
            for (j,type) in enumerate(row):
                print  i,j,type
                if(type == lastType and lastType==" "):
                    pass
                else:
                    self.bl_list.add(self.makeBlock(type,j,i))
                    lastType = "#";

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

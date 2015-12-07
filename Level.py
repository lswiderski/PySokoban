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

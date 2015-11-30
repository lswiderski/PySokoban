__author__ = 'neufrin'
import pygame
import Block
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (128,128,128)

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PySokoban')
clock = pygame.time.Clock()


Map = ["#####", "#@  #", "# $.#", "# $.#", "#####"]
Map2 = ["  ####", "### @#","#    #","# .#.###","# $    #","##*#*# #","# $    #","#   ####", "#####"]


bl_list = pygame.sprite.Group()
#bl_list.add(Block.Block("Wall", 2, 0))
#bl_list.add(Block.Block("Floor", 3, 1))
#bl_list.add(Block.Block("Player", 4, 2))
#bl_list.add(Block.Block("Goal", 5, 3))
#bl_list.add(Block.Block("Box", 6, 4))
#bl_list.add(Block.Block("Empty", 7, 5))

for (i,row) in enumerate(Map2):
    for (j,type) in enumerate(row):
        print  i,j,type
        bl_list.add(Block.Block(type, j, i))
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    gameDisplay.fill(WHITE)
    bl_list.draw(gameDisplay)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
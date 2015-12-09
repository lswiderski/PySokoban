__author__ = 'neufrin'
import pygame
import Level

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (128,128,128)

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PySokoban')
clock = pygame.time.Clock()

screens = {"level" : Level.Level(),
           "mainmenu" : Level.Level(),
           "finishedlevel" : Level.Level(),
           "levelselect" : Level.Level(),
           "options" : Level.Level(),
           "scredits" : Level.Level(),
          }
actualscreen = "level"

crashed = False
while not crashed:
    events = pygame.event.get()
    gameDisplay.fill(WHITE)
    crashed = screens[actualscreen].play(events,gameDisplay)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()

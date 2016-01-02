__author__ = 'neufrin'
import pygame

import Helper
import Screens


WHITE = (128,128,128)

pygame.init()
gameDisplay = pygame.display.set_mode((Helper.SCREEN_WIDTH,Helper.SCREEN_HEIGHT))
pygame.display.set_caption('PySokoban')
clock = pygame.time.Clock()

bgm = 'Content/background.wav'
pygame.mixer.init()
pygame.mixer.music.load(bgm)
pygame.mixer.music.play(-1, 0.0)


crashed = False
while not crashed:
    events = pygame.event.get()
    gameDisplay.fill(WHITE)
    crashed = Screens.screens[Helper.actualscreen].play(events,gameDisplay)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()

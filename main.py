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


level = Level.Level()
crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    gameDisplay.fill(WHITE)
    level.draw(gameDisplay)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
quit()
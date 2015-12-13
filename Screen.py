__author__ = 'neufrin'
import pygame




class Screen(object):
    def __init__(self,name):
        self.name=name
        self.empty_list = pygame.sprite.Group()

    def update(self,events):
        crashed = False
        for event in events:
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        return crashed

    def draw(self,screen):
        self.empty_list.draw(screen)

    def play(self,events,screen):
        self.draw(screen)
        crashed =  self.update(events)

        return crashed
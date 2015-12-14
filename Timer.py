__author__ = 'neufrin'
import pygame

WHITE = (255, 255, 255)


class Timer():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.frame_rate = 60
        self.time =""

    def restart(self):
        self.frame_count = 0

    def update(self):
        total_seconds = self.frame_count // self.frame_rate
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        self.time = "Time: {0:02}:{1:02}".format(minutes, seconds)
        self.frame_count += 1
        self.clock.tick(self.frame_rate)

    def draw(self,screen,font):
        text = font.render(self.time, True, WHITE)
        screen.blit(text, [600, 10])

import pygame
from pygame.locals import *
pygame.init()

class Paddle(pygame.sprite.Sprite):
    "Paddle metadata"
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.change = 0

    def move(self):
        self.rect.x += self.change

    def stop(self):
        self.rect.x += 0

    def inc_change(self, change):
        self.change = change

    def check_left_boundary(self):
        if self.rect.x + self.change <= 0:
            return True

    def check_right_boundary(self):
        if self.rect.x + self.change >= 900:
            return True

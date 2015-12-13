import pygame
from pygame.locals import *
pygame.init()

class Brick(pygame.sprite.Sprite):
    "Brick Metadata"
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

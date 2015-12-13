import pygame
from pygame.locals import *
import space_colors, space_screen, space_ship

class Invader(pygame.sprite.Sprite):
    "Metadata for Invaders"
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = pygame.transform.scale(self.image, (100, 125))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 2
        self.drop = 25

    def move(self):
        self.rect.centerx += self.speed

    def drop_down(self):
        self.rect.centery += self.drop

    def increase_speed(self):
        if self.speed < 0:
            self.speed -= 1
        elif self.speed >= 0:
            self.speed += 1

    def reverse_direction(self):
        self.speed *= -1


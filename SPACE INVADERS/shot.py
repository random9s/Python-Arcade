import pygame, sys, space_ship, invaders
from pygame.locals import *
pygame.init()

class Shot(pygame.sprite.Sprite):
    "Metadata for Shots from Player and enemies"
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.y -= 50

    def destroy(self, enemies):
        destroyed = False
        if self.off_screen() or self.hit_enemy(enemies):
            destroyed = True
        return destroyed

    def off_screen(self):
        if self.rect.y <= 20:
            return True

    def hit_enemy(self, enemies):
        enemies_hit = pygame.sprite.spritecollide(self, enemies, True)
        if enemies_hit:
            return True

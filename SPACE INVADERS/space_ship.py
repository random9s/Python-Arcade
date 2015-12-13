import pygame
from pygame.locals import *
import sys, space_colors, space_screen, shot
pygame.init()

class Spaceship(pygame.sprite.Sprite):
    "Metadata for spaceship"
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change = 0
        self.shot_bag = pygame.sprite.Group()

    def move(self):
        self.rect.x += self.change

    def inc_change(self, change):
        self.change = change

    def shoot(self, shot_img):
        self.shot_bag.add(shot.Shot(shot_img, self.rect.centerx-23, self.rect.centery-40))

    def shot_exists(self):
        if(self.shot_bag.has(self.shot_bag)):
            return True

    def check_shot_destroyed(self, enemies, score):
        destroyed = False
        if(self.shot_bag.has(self.shot_bag)):
            for shot in self.shot_bag:
                destroyed = shot.destroy(enemies)
                if destroyed:
                    score += 10
                    shot.kill()
        return score

    def destroy(self):
        None #Todo

    def restart(self):
        None #Todo

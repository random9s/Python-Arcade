import pygame
from pygame.locals import *
pygame.init()

class Ball(pygame.sprite.Sprite):
    "Ball metadata"
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.change_x = 6
        self.change_y = 15

    def move(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def check_for_wall_hit(self):
        if self.rect.x <= 0:
            if self.change_x < 0 and self.change_y < 0:
                self.change_x_and_y(6, -15)
            elif self.change_x < 0 and self.change_y >= 0:
                self.change_x_and_y(6, 15)
        elif self.rect.x >= 980:
            if self.change_x >= 0 and self.change_y < 0:
                self.change_x_and_y(-6, -15)
            elif self.change_x >= 0 and self.change_y >= 0:
                self.change_x_and_y(-6, 15)

    def paddle_hit(self, paddle):
        if self.rect.right >= paddle.left and self.rect.right <= paddle.left + 33:
            self.change_x_and_y(-6, -15)
        elif self.rect.right >= paddle.left + 33 and self.rect.centerx <= paddle.left + 66:
            self.change_x_and_y(0, -15)
        elif self.rect.centerx >= paddle.left + 66 and self.rect.left <= paddle.right:
            self.change_x_and_y(6, -15)

    def brick_hit(self):
        if self.change_x < 0 and self.change_y < 0:
            self.change_x_and_y(-6, 15)
        elif self.change_x >= 0 and self.change_y < 0:
            self.change_x_and_y(6, 15)
        elif self.change_x < 0 and self.change_y >= 0:
            self.change_x_and_y(-6, -15)
        elif self.change_x >= 0 and self.change_y >= 0:
            self.change_x_and_y(6, 15)

    def change_x_and_y(self, changex, changey):
        self.change_x = changex
        self.change_y = changey

    def check_off_screen(self):
        if self.rect.top >= 700 or self.rect.bottom <= 0:
            return True

    def reset(self):
        self.rect.x = 490
        self.rect.y = 350
        self.change_x = 6
        self.change_y = 15

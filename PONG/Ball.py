import pygame
from pygame.locals import *
pygame.init()
import pong_sound

class Ball():
    "Game Ball metadata"
    def __init__(self, x, y, change_x, change_y, velocity, size, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.velocity = velocity
        self.size = size
        self.color = color

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, [self.x,self.y, self.size, self.size])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def check_for_wall_hit(self):
        if self.y > 590 or self.y < 0:
            self.change_y *= -1
            pong_sound.play_wall()

    def check_for_paddle_hit(self, b_dim, p1_dim, p2_dim):
        if b_dim.colliderect(p1_dim):
            if b_dim.bottom >= p1_dim.top and b_dim.bottom <= p1_dim.bottom-40:
                self.change_x = 10
                self.change_y = -5
            elif b_dim.top >= p1_dim.bottom-39 and b_dim.bottom <= p1_dim.bottom-20:
                self.change_x = 15
                self.change_y = 0
            else:
                self.change_x = 10
                self.change_y = 5
            pong_sound.play_ping()

        if b_dim.colliderect(p2_dim):
            if b_dim.bottom >= p2_dim.top and b_dim.bottom <= p2_dim.bottom-40:
                self.change_x = -10
                self.change_y = -5
            elif b_dim.top >= p2_dim.bottom-39 and b_dim.bottom <= p2_dim.bottom-20:
                self.change_x = -15
                self.change_y = 0
            else:
                self.change_x = -10
                self.change_y = 5
            pong_sound.play_ping()

    def check_for_score(self):
        if self.x > 790:
            return 1
        elif self.x < 0:
            return 2

    def reset(self):
        self.x = 350
        self.y = 220
        self.change_x = 10
        self.change_y = 5
        self.velocity = -1

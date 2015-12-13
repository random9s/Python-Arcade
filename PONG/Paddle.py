import pygame
from pygame.locals import *
import Ball, pong_colors
pygame.init()
class Paddle():
    "Metadata for game paddles"
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.change = 0

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, [self.x, self.y, self.height, self.width])

    def move(self):
        self.y += self.change

    def stop(self):
        self.y += 0

    def inc_change(self, change):
        self.change = change

    def slow_down(self):
        self.y += self.change

    def check_top_boundary(self):
        if self.y + self.change <= 0:
            return True

    def check_bottom_boundary(self):
        if self.y + self.change >= 540:
            return True

    def print_attributes(self):
        print "Paddle x: ", self.x
        print "Paddle y: ", self.y

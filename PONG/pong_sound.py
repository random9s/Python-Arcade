import pygame, sys
from pygame.locals import *
import time

pygame.init()

def play_ping():
    try:
        ping = pygame.mixer.Sound('pong_sounds/ping.mp3')
        ping.play()
        return ping
    except pygame.error, message:
        print "Cannot load ping"


def play_wall():
    try:
        wall = pygame.mixer.Sound('pong_sounds/wall.mp3')
        wall.play()
        return wall
    except pygame.error, message:
        print "Cannot load wall ping"

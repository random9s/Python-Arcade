import pygame, sys
from pygame.locals import *
pygame.init()

def getNet(COLOR, SCREEN):
    pygame.draw.line(SCREEN, COLOR, (0,0), (0,598), 2)
    pygame.draw.line(SCREEN, COLOR, (0,0), (798,0), 2)
    pygame.draw.line(SCREEN, COLOR, (798,0), (798,598), 2)
    pygame.draw.line(SCREEN, COLOR, (0,598), (798,598), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 0), (400, 20), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 30), (400, 50), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 60), (400, 80), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 90), (400, 110), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 120), (400, 140), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 150), (400, 170), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 180), (400, 200), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 210), (400, 230), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 240), (400, 260), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 270), (400, 290), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 300), (400, 320), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 330), (400, 350), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 360), (400, 380), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 390), (400, 410), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 420), (400, 440), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 450), (400, 470), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 480), (400, 500), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 510), (400, 530), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 540), (400, 560), 2)
    pygame.draw.line(SCREEN, COLOR, (400, 570), (400, 590), 2)

def getScorePlayer1(SCORE, COLOR, SCREEN):
    if SCORE == 0:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 120), (220, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 120), (220, 30), 4)
    elif SCORE == 1:
        pygame.draw.line(SCREEN, COLOR, (200, 30), (200, 120), 4)
    elif SCORE == 2:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (180, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 120), (220, 120), 4)
    elif SCORE == 3:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (180, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (220, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 120), (220, 120), 4)
    elif SCORE == 4:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 70), (220, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 70), (220, 120), 4)
    elif SCORE == 5:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (220, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 120), (180, 120), 4)
    elif SCORE == 6:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (220, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 120), (220, 120), 4)
    elif SCORE == 7:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 120), 4)
    elif SCORE == 8:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (220, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 75), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 75), (220, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 120), (220, 120), 4)
    elif SCORE == 9:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (220, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (180, 70), (220, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 70), (220, 120), 4)
    elif SCORE == 10:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (200, 30), (240, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (200, 30), (200, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (240, 30), (240, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (200, 120), (240, 120), 4)
    elif SCORE == 11:
        pygame.draw.line(SCREEN, COLOR, (180, 30), (180, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (220, 30), (220, 120), 4)

def getScorePlayer2(SCORE, COLOR, SCREEN):
    if SCORE == 0:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 120), (620, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 120), (620, 30), 4)
    elif SCORE == 1:
        pygame.draw.line(SCREEN, COLOR, (600, 30), (600, 120), 4)
    elif SCORE == 2:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (580, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 120), (620, 120), 4)
    elif SCORE == 3:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (580, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (620, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 120), (620, 120), 4)
    elif SCORE == 4:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 70), (620, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 70), (620, 120), 4)
    elif SCORE == 5:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (620, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 120), (580, 120), 4)
    elif SCORE == 6:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (620, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 120), (620, 120), 4)
    elif SCORE == 7:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 120), 4)
    elif SCORE == 8:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (620, 75), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 75), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 75), (620, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 120), (620, 120), 4)
    elif SCORE == 9:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (620, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (580, 70), (620, 70), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 70), (620, 120), 4)
    elif SCORE == 10:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (600, 30), (640, 30), 4)
        pygame.draw.line(SCREEN, COLOR, (600, 30), (600, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (640, 30), (640, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (600, 120), (640, 120), 4)
    elif SCORE == 11:
        pygame.draw.line(SCREEN, COLOR, (580, 30), (580, 120), 4)
        pygame.draw.line(SCREEN, COLOR, (620, 30), (620, 120), 4)

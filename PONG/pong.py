import pygame, sys
from pygame.locals import *
import pong_score
import pong_colors
import pong_sound
import time

def set_screen(play1, play2, screen):
    screen.fill(pong_colors.BLACK)
    pong_score.getNet(pong_colors.GREEN, screen)
    pong_score.getScorePlayer1(play1.score, pong_colors.WHITE, screen)
    pong_score.getScorePlayer2(play2.score, pong_colors.WHITE, screen)

def get_events(pad1, pad2):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                    pad1.inc_change(-6)
            elif event.key == pygame.K_s:
                    pad1.inc_change(6)
            if event.key == pygame.K_UP:
                    pad2.inc_change(-6)
            elif event.key == pygame.K_DOWN:
                    pad2.inc_change(6)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                pad1.inc_change(0)
            elif event.key == pygame.K_s:
                pad1.inc_change(0)
            if event.key == pygame.K_UP:
                pad2.inc_change(0)
            elif event.key == pygame.K_DOWN:
                pad2.inc_change(0)

def movement(pad1, pad2, ball):
    #move paddle 1
    if pad1.check_top_boundary():
        pad1.stop()
    elif pad1.check_bottom_boundary():
        pad1.stop()
    else:
        pad1.move()
    #move paddle 2
    if pad2.check_top_boundary():
        pad2.stop()
    elif pad2.check_bottom_boundary():
        pad2.stop()
    else:
        pad2.move()
    #move ball
    ball.move()


def scored(play1, play2, ball):
    if(ball.check_for_score() == 1):
        play1.scored()
        ball.reset()
    elif(ball.check_for_score() == 2):
        play2.scored()
        ball.reset()

def game_over(play1, play2):
    if(play1.score == 11 or play2.score == 11):
        return True



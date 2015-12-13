import pygame
from pygame.locals import *
import Brick, Paddle, Ball, breakout_colors, breakout, sys

pygame.init()
pygame.font.init()

def get_events(paddle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.inc_change(-6)
            elif event.key == pygame.K_RIGHT:
                paddle.inc_change(6)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle.inc_change(0)
            elif event.key == pygame.K_RIGHT:
                paddle.inc_change(0)

def movement(paddle, ball):
    if paddle.check_left_boundary():
        paddle.stop()
    elif paddle.check_right_boundary():
        paddle.stop()
    else:
        paddle.move()
    ball.move()

def game_screen(screen, score, lives):
    screen.fill(breakout_colors.BLACK)
    score_font = pygame.font.SysFont("monospace", 20)
    label = score_font.render("Score: ", 1, breakout_colors.WHITE)
    screen.blit(label, (15, 3))
    score_label = score_font.render(str(score), 1, breakout_colors.WHITE)
    screen.blit(score_label, (90, 3))

    offset = 0
    while lives != 0:
        pygame.draw.rect(screen, breakout_colors.WHITE, (900 + offset, 5, 15, 15))
        offset += 30
        lives -= 1

def play(bricks, sprites, ball, paddle, score, lives, clock, screen):
    while True:
        if lives <= 0:
            break
        #Draw the screen, including lives and score
        breakout.game_screen(screen, score, lives)
        #Did the ball hit the wall
        ball.check_for_wall_hit()
        #Did player lose life
        if ball.check_off_screen():
            lives -= 1
            ball.reset()
        #Did the ball hit the bricks
        collide_bricks = pygame.sprite.spritecollide(ball, bricks, True)
        if collide_bricks:
            ball.brick_hit()
            score += 20
        #Did the ball hit the paddle
        if ball.rect.colliderect(paddle.rect):
            ball.paddle_hit(paddle.rect)
        sprites.draw(screen)
        #Handle events and movement
        breakout.get_events(paddle)
        breakout.movement(paddle, ball)
        clock.tick(30)
        pygame.display.update()



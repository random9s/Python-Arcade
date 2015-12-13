import pygame
from pygame.locals import *
import sys, time
import Brick, Paddle, Ball, breakout_colors, breakout

def replay(screen):
    while True:
        screen.fill(breakout_colors.BLACK)
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render("Game over!", 1, (0,255,0))
        screen.blit(label, (430,300))
        label2 = myfont.render("Replay? [y / n]", 1, (0,255,0))
        screen.blit(label2, (400, 350))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    main()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_y:
                    main()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Breakout")
    screen_width = 1000
    screen_height = 700
    screen = pygame.display.set_mode((screen_width,screen_height))
    score = 0
    lives = 3
    bricks = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    x = 0
    y = 25

    for i in range(60):
        #Create different color blocks
        if i >= 0 and i <= 9:
            brick = Brick.Brick(breakout_colors.RED, 100, 25)
        elif i >= 10 and i <= 19:
            brick = Brick.Brick(breakout_colors.ORANGE, 100, 25)
        elif i >= 20 and i <= 29:
            brick = Brick.Brick(breakout_colors.DARK_ORANGE, 100, 25)
        elif i >= 30 and i <= 39:
            brick = Brick.Brick(breakout_colors.YELLOW, 100, 25)
        elif i >= 40 and i <= 49:
            brick = Brick.Brick(breakout_colors.GREEN, 100, 25)
        elif i >= 50 and i <= 59:
            brick = Brick.Brick(breakout_colors.BLUE, 100, 25)

        brick.rect.x = x
        brick.rect.y = y
        #Add bricks to lists
        bricks.add(brick)
        all_sprites.add(brick)
        #Increment x and y values
        x+=100
        if (i+1) % 10 == 0:
            x=0
            y+=25

    ball = Ball.Ball(breakout_colors.WHITE, 20, 20)
    ball.rect.x = 490
    ball.rect.y = 350
    all_sprites.add(ball)

    paddle = Paddle.Paddle(breakout_colors.WHITE, 100, 15)
    paddle.rect.x = 450
    paddle.rect.y = 650
    all_sprites.add(paddle)

    clock = pygame.time.Clock()
    breakout.play(bricks, all_sprites, ball, paddle, score, lives, clock, screen)
    replay(screen)

if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *
import sys, Ball, Paddle, pong_colors, Player, pong_score, pong

def replay(screen):
    while True:
        screen.fill(pong_colors.BLACK)
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render("Game over!", 1, (0,255,0))
        screen.blit(label, (340,230))
        label2 = myfont.render("Replay? [y / n]", 1, (0,255,0))
        screen.blit(label2, (300, 290))

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

def play(screen, ball, pad1, pad2, play1, play2, clock):
    while True:
        pong.set_screen(play1, play2, screen)
        #Is the game over?
        if (pong.game_over(play1, play2)):
            break
        #Draw objects once they move
        b_dim = ball.draw(screen)
        p1_dim = pad1.draw(screen)
        p2_dim = pad2.draw(screen)
        #Check for object hits
        ball.check_for_wall_hit()
        ball.check_for_paddle_hit(b_dim, p1_dim, p2_dim)
        #Check if player scored
        pong.scored(play1, play2, ball)
        #Get events
        pong.get_events(pad1, pad2)
        #Move Game Objects
        pong.movement(pad1, pad2, ball)
        #Update the display
        pygame.display.update()
        clock.tick(30)

def main():
    pygame.init()
    pygame.display.set_caption("Pong!")
    screen = pygame.display.set_mode((800,600))
    gameball = Ball.Ball(350, 220, 10, 5, -1, 10, pong_colors.WHITE)
    paddle1 = Paddle.Paddle(15, 300, 15, 60, pong_colors.WHITE)
    paddle2 = Paddle.Paddle(755, 300, 15, 60, pong_colors.WHITE)
    player1 = Player.Player(0, 1)
    player2 = Player.Player(0, 2)
    clock = pygame.time.Clock()
    play(screen, gameball, paddle1, paddle2, player1, player2, clock)
    replay(screen)

if __name__ == "__main__":
    main()

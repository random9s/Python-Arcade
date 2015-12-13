import pygame
from pygame.locals import *
import sys, time
import space_colors, space_screen, space_ship, invaders

def play(screen, IMAGES, enemies, fighter, all_sprites, score, lives, clock):
    while True:
        if not enemies.has(enemies) or space_screen.invader_touching_bottom(enemies)  or lives == 0:
            print "Game Over!"
            break
        space_screen.get_screen(screen, lives, score)
        all_sprites.draw(screen)
        space_screen.handle_events(fighter, IMAGES)
        score = space_screen.shots_fired(screen, fighter, enemies, score)
        space_screen.movement(fighter, enemies)
        pygame.display.update()
        clock.tick(30)

def main():
    pygame.init()
    pygame.display.set_caption("Space Invaders")
    IMAGES = {'invader-a': pygame.image.load('sprites/spaceinvaderA.png'),
              'invader-b': pygame.image.load('sprites/spaceinvaderB.png'),
              'invader-c': pygame.image.load('sprites/spaceinvaderC.png'),
              'mothership': pygame.image.load('sprites/mothership.png'),
              'spaceship': pygame.image.load('sprites/spacefighter.png'),
              'shield': pygame.image.load('sprites/shield.png'),
              'shot': pygame.image.load('sprites/shot.png'),
              'zigshot': pygame.image.load('sprites/zigshot.png')}
    screen = space_screen.screen_start()
    enemies = space_screen.create_invaders(screen, IMAGES['invader-a'], IMAGES['invader-b'], IMAGES['invader-c'], 150, 100)
    fighter = space_screen.create_fighter(screen, IMAGES['spaceship'])
    all_sprites = space_screen.get_all_sprites(enemies, fighter)
    clock = pygame.time.Clock()
    play(screen, IMAGES, enemies, fighter, all_sprites, 0, 3, clock)

if __name__ == "__main__":
    main()

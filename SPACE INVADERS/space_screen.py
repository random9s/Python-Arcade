import pygame
from pygame.locals import *
import sys, time, space_colors, space_ship, player, invaders

def screen_start():
    size = (1200,750)
    return pygame.display.set_mode(size)

def get_screen(screen, lives, score):
    black_screen(screen)
    display_score(screen, score)
    display_lives(screen, lives)

def black_screen(screen):
    screen.fill(space_colors.BLACK)

def create_invaders(screen, invader_a, invader_b, invader_c, x, y):
    enemies = pygame.sprite.Group()
    for i in range(50):
        if i >= 0 and i < 10:
            invader = invaders.Invader(invader_c, x-35, y)
        elif i >= 10 and i < 30:
            if i == 10 or i == 20:
                x = 100
                y += 50
            invader = invaders.Invader(invader_b, x, y)
        elif i >= 30 and i < 50:
            if i == 30 or i == 40:
                x = 100
                y += 50
            invader = invaders.Invader(invader_a, x, y)
        enemies.add(invader)
        x += 80
    return enemies

def create_mothership(screen, mothership):
    return invaders.Invader(mothership, 0, 20)

def create_fighter(screen, spaceship):
    return space_ship.Spaceship(spaceship, 550, 650)

def create_shields(screen):
    None

def get_all_sprites(enemies, fighter):
    all_sprites = pygame.sprite.Group()
    for enemy in enemies:
        all_sprites.add(enemy)
    all_sprites.add(fighter)
    return all_sprites

def display_lives(screen, lives):
    font = pygame.font.Font(None, 24)
    text = font.render("Lives: ", 1, (0, 255, 0))
    textpos = text.get_rect()
    textpos.x = 1000
    textpos.y = 20
    screen.blit(text, textpos)
    text1 = font.render(str(lives), 1, (0, 255, 0))
    textpos1 = text.get_rect()
    textpos1.x = 1060
    textpos1.y = 20
    screen.blit(text1, textpos1)

def display_score(screen, score):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: ", 1, (0,255,0))
    textpos = text.get_rect()
    textpos.x = 25
    textpos.y = 20
    screen.blit(text, textpos)
    text1 = font.render(str(score), 1, (0, 255, 0))
    textpos1 = text.get_rect()
    textpos1.x = 90
    textpos1.y = 20
    screen.blit(text1, textpos1)

def shots_fired(screen, fighter, enemies, score):
    if fighter.shot_bag.has(fighter.shot_bag):
        fighter.shot_bag.draw(screen)
        for shot in fighter.shot_bag:
            shot.move()
    return fighter.check_shot_destroyed(enemies, score)

def movement(fighter, enemies):
    fighter.move()

    if invader_touching_left_wall(enemies):
        enemies_drop_down(enemies)
        enemies_move_right(enemies)
    elif invader_touching_right_wall(enemies):
        enemies_drop_down(enemies)
        enemies_move_left(enemies)
    move_enemy(enemies)

def enemies_drop_down(enemies):
    for enemy in enemies:
        enemy.drop_down()
        enemy.increase_speed()

def move_enemy(enemies):
    for enemy in enemies:
        enemy.move()

def enemies_move_left(enemies):
    for enemy in enemies:
        enemy.reverse_direction()

def enemies_move_right(enemies):
    for enemy in enemies:
        enemy.reverse_direction()

def invader_touching_left_wall(enemies):
    touching = False
    for enemy in enemies:
        if enemy.rect.left <= 0:
            touching = True
    return touching

def invader_touching_right_wall(enemies):
    touching = False
    for enemy in enemies:
        if enemy.rect.right >= 1200:
            touching = True
    return touching

def invader_touching_bottom(enemies):
    for enemy in enemies:
        if enemy.rect.bottom >= 750:
            return True

def handle_events(fighter, IMAGES):
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()

    LEFT = pygame.key.get_pressed()[pygame.K_LEFT]
    RIGHT = pygame.key.get_pressed()[pygame.K_RIGHT]
    SHOOT = pygame.key.get_pressed()[pygame.K_SPACE]

    if LEFT == 1 and RIGHT == 0:
        fighter.inc_change(-8)
    elif RIGHT == 1 and LEFT == 0:
        fighter.inc_change(8)
    if RIGHT == 0 and LEFT == 0:
        fighter.inc_change(0)
    if SHOOT == 1:
        if not fighter.shot_exists():
            fighter.shoot(IMAGES['shot'])


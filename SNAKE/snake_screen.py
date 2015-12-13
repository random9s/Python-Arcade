import pygame, sys
from pygame.locals import *


def drawPressKeyMsg(SCREEN, BASICFONT, DARKGRAY, display_width, display_height):
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (display_width - 200, display_height - 30)
    SCREEN.blit(pressKeySurf, pressKeyRect)

def terminate():
    pygame.quit()
    sys.exit()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen(BGCOLOR, WHITE, DARKGREEN, DARKGRAY, BASICFONT, SCREEN, display_width, display_height, FPSCLOCK, FPS):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snake!', True, WHITE)

    degrees1 = 0
    degrees2 = 0
    while True:
        SCREEN.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (display_width / 2, display_height / 2)
        SCREEN.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (display_width / 2, display_height / 2)
        SCREEN.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg(SCREEN, BASICFONT, DARKGRAY, display_width, display_height)

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def showGameOverScreen(SCREEN, BASICFONT, DARKGRAY, WHITE, display_width, display_height):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (display_width / 2, 100)
    overRect.midtop = (display_width / 2, gameRect.height + 100 + 25)

    SCREEN.blit(gameSurf, gameRect)
    SCREEN.blit(overSurf, overRect)
    drawPressKeyMsg(SCREEN, BASICFONT, DARKGRAY, display_width, display_height)
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

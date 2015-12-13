import random, pygame, sys
from pygame.locals import *
import snake_screen

FPS = 15
display_width = 640
display_height = 480
cell_size = 20
assert display_width % cell_size == 0, "Window width must be a multiple of cell size."
assert display_height % cell_size == 0, "Window height must be a multiple of cell size."
cell_width = int(display_width / cell_size)
cell_height = int(display_height / cell_size)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, SCREEN, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((display_width, display_height))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    snake_screen.showStartScreen(BGCOLOR, WHITE, DARKGREEN, DARKGRAY, BASICFONT, SCREEN, display_width, display_height, FPSCLOCK, FPS)
    while True:
        runGame()
        snake_screen.showGameOverScreen(SCREEN, BASICFONT, DARKGRAY, WHITE, display_width, display_height)


def runGame():
    # Set a random start point.
    startx = random.randint(5, cell_width - 6)
    starty = random.randint(5, cell_height - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the apple in a random place.
    apple = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                snake_screen.terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    snake_screen.terminate()

        # check if the worm has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == cell_width or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == cell_height:
            return # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return # game over

        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
        else:
            del wormCoords[-1] # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        SCREEN.fill(BGCOLOR)
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomLocation():
    return {'x': random.randint(0, cell_width - 1), 'y': random.randint(0, cell_height - 1)}

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (display_width - 120, 10)
    SCREEN.blit(scoreSurf, scoreRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * cell_size
        y = coord['y'] * cell_size
        wormSegmentRect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(SCREEN, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cell_size - 8, cell_size - 8)
        pygame.draw.rect(SCREEN, GREEN, wormInnerSegmentRect)

def drawApple(coord):
    x = coord['x'] * cell_size
    y = coord['y'] * cell_size
    appleRect = pygame.Rect(x, y, cell_size, cell_size)
    pygame.draw.rect(SCREEN, RED, appleRect)

if __name__ == '__main__':
    main()

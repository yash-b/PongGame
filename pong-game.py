import pygame
import sys
import time
import random

pygame.init()
main_clock = pygame.time.Clock()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("PONG GAME")
clock = pygame.time.Clock()

DOWN_LEFT = 'downleft'
DOWN_RIGHT = 'downright'
UP_LEFT = 'upleft'
UP_RIGHT = 'upright'


MOVE_SPEED = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_pong_single = {'rect':pygame.Rect(300, 80, 50, 100), 'color':WHITE, 'dir':UP_RIGHT}

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUT:
            pygame.quit()
            sys.exit()

    # ToDO:
    #  [ ] Game Logic -> Collision Detector -> Score
    #  [ ] Sprites & Sound

    surface.fill(BLACK)

    pygame.draw.line(surface, WHITE, [399, 0], [399, 500], 3)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



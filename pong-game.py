import pygame
import sys
import time
import random
from .objects.paddles import Paddle

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

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)

player_pong_single = {'rect':pygame.Rect(300, 80, 50, 100), 'color':WHITE, 'dir':UP_RIGHT}

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_w:
                paddleA.

    # ToDO:
    #  [ ] Game Logic -> Collision Detector -> Score
    #  [ ] Sprites & Sound

    surface.fill(BLACK)

    pygame.draw.line(surface, WHITE, [399, 0], [399, 500], 3)
    sprites_list.draw(surface)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()



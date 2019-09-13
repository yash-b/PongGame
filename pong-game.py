import pygame
import sys
import time
import random

pygame.init()
main_clock = pygame.time.Clock()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

WHITE = (255, 255, 255)

player_pong_single = pygame.Rect()
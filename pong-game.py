import pygame
import sys
from .objects.paddles import Paddle
from .objects.ball import Ball

#  ToDO
# - [ ] Ball reset
# - [ ] AI Implementaion
# - [ ] Sounds & Sprites
# - [ ] Top and bottom paddles
# - [ ] Scoring and max limit to score


pygame.init()
main_clock = pygame.time.Clock()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("PONG GAME")
clock = pygame.time.Clock()

DOWN_LEFT, DOWN_RIGHT, UP_LEFT,  UP_RIGHT = 'downleft', 'downright', 'upleft', 'upright'
MOVE_SPEED = 4

WHITE, BLACK = (255, 255, 255), (0, 0, 0)


paddle_one = Paddle(WHITE, 10, 100)
paddle_one.rect.x, paddle_one.rect.y = 20, 200

paddle_two = Paddle(WHITE, 10, 100)
paddle_two.rect.x, paddle_two.rect.y = 770, 200


ball = Ball(WHITE, 10, 10)
ball.rect.x, ball.rect.y = 395, 195

sprites_list = pygame.sprite.Group()
sprites_list.add(paddle_one)
sprites_list.add(paddle_two)
sprites_list.add(ball)

PLAYER_SCORE, AI_SCORE = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.locals.KEYDOWN:
            if event.type == pygame.locals.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.locals.K_w:
                paddle_one.move_up(5)
            if event.key == pygame.locals.K_s:
                paddle_one.move_down(5)
        sprites_list.update()

        if ball.rect.x >= 795:
            PLAYER_SCORE += 1
            # RESET BALL

        elif ball.rect.x <= 0:
            AI_SCORE += 1
            # RESET BALL

        if ball.rect.y > 490 and ball.rect.x >= 395:
            PLAYER_SCORE += 1
            # RESET BALL

        elif ball.rect.y > 490 and ball.rect.x < 395:
            AI_SCORE += 1
            # RESET BALL

        if ball.rect.y < 0 and ball.rect.x >= 395:
            PLAYER_SCORE += 1
            # RESET BALL

        elif ball.rect.y < 0 and ball.rect.x < 395:
            AI_SCORE += 1
            # RESET BALL
        if pygame.sprite.collide_mask(ball, paddle_one) or pygame.sprite.collide_mask(ball, paddle_two):
            ball.bounce()

    surface.fill(BLACK)

    pygame.draw.line(surface, WHITE, [399, 0], [399, 500], 3)
    sprites_list.draw(surface)

    font = pygame.font.Font(None, 74)
    text = font.render(str(PLAYER_SCORE), 1, WHITE)
    surface.blit(text, (250, 10))
    text = font.render(str(AI_SCORE), 1, WHITE)
    surface.blit(text, (420, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



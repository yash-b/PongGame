import pygame
import sys
import random
from pygame.locals import *


#  ToDO
# - [X] Ball reset
# - [X] AI Implementation
# - [X] Sounds & Sprites
# - [X] Top and bottom paddles
# - [X] Scoring and max limit to score

MOVE_SPEED = 5
WHITE, BLACK, GREEN = (255, 255, 255), (0, 0, 0), (57, 255, 20)
pos_ball, vel_ball, radius_ball = [0, 0], [0, 0], 3.5
vel_x, vel_y = 0, 0

pygame.init()
main_clock = pygame.time.Clock()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("PONG GAME")
font_arial = pygame.font.SysFont("Arial", 18)
paddle_image = pygame.image.load('resources/paddle.png')
paddle_resize_one = pygame.transform.scale(paddle_image, (8, 100))
paddle_resize_two = pygame.transform.scale(paddle_image, (100, 8))
pong_collide_sound = pygame.mixer.Sound('resources/collision.wav')
point_scored_sound = pygame.mixer.Sound('resources/point_scored.wav')
game_won_sound = pygame.mixer.Sound('resources/game_won.wav')
game_lost_sound = pygame.mixer.Sound('resources/game_lost.wav')
winner_winner_player = pygame.mixer.Sound('resources/player_wins.wav')
pygame.mixer.music.load('resources/background_music.wav')


pos_paddle_one = [4, WINDOW_HEIGHT // 2]
pos_paddle_two = [0, 0]
pos_paddle_three = [0, 395]
pos_paddle_four = [786, WINDOW_HEIGHT // 2]
pos_paddle_five = [700, 1]
pos_paddle_six = [700, 395]

paddle_one = pygame.Rect(0, WINDOW_HEIGHT // 2, 8, 100)
paddle_two = pygame.Rect(0, 1, 100, 8)
paddle_three = pygame.Rect(0, 390, 100, 8)
paddle_four = pygame.Rect(790, WINDOW_HEIGHT // 2, 8, 100)
paddle_five = pygame.Rect(700, 1, 100, 8)
paddle_six = pygame.Rect(700, 390, 100, 100)
ball = pygame.draw.circle(surface, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 10)

PLAYER_SCORE, AI_SCORE, PLAYER_GAMES_WON, AI_GAMES_WON = 0, 0, 0, 0
MAX_SCORE_PLAYER, MAX_SCORE_AI = 11, 11


def reset_pong(rand):
    global pos_ball, vel_ball, vel_x, vel_y
    pos_ball = [WINDOW_WIDTH // 2, random.randrange(100, 400, 100)]
    vel_x = random.randrange(2, 5)
    vel_y = random.randrange(-5, 5)
    if not rand:
        vel_x = -vel_x
    vel_ball = [vel_x, -vel_y]


def continue_game():
    while True:
        for events in pygame.event.get():
            if events.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if events.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return


while True:

    if random.randrange(0, 2) == 0:
        reset_pong(True)
    else:
        reset_pong(False)

    go_left, go_right, go_up, go_down = 0, 0, 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.locals.KEYDOWN:
                if event.type == pygame.locals.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.locals.K_UP:
                    go_down = False
                    go_up = True
                if event.key == pygame.locals.K_DOWN:
                    go_up = False
                    go_down = True
                if event.key == pygame.locals.K_LEFT:
                    go_right = False
                    go_left = True
                if event.key == pygame.locals.K_RIGHT:
                    go_left = False
                    go_right = True

            if event.type == pygame.locals.KEYUP:
                if event.key == pygame.locals.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.locals.K_LEFT:
                    go_left = False
                if event.key == pygame.locals.K_RIGHT:
                    go_right = False
                if event.key == pygame.locals.K_UP:
                    go_up = False
                if event.key == pygame.locals.K_DOWN:
                    go_down = False

        if go_down and paddle_one.bottom < WINDOW_HEIGHT:
            paddle_one.top += MOVE_SPEED
            pos_paddle_one[1] += MOVE_SPEED
        if go_up and paddle_one.top > 0:
            paddle_one.top -= MOVE_SPEED
            pos_paddle_one[1] -= MOVE_SPEED
        if go_left and paddle_two.left > 0 and paddle_three.left > 0:
            paddle_three.left -= MOVE_SPEED
            paddle_two.left -= MOVE_SPEED
            pos_paddle_two[0] -= MOVE_SPEED
            pos_paddle_three[0] -= MOVE_SPEED
        if go_right and paddle_two.right < WINDOW_WIDTH // 2 and paddle_three.right < WINDOW_WIDTH // 2:
            paddle_three.right += MOVE_SPEED
            paddle_two.right += MOVE_SPEED
            pos_paddle_one[0] += MOVE_SPEED
            pos_paddle_three[0] += MOVE_SPEED

        pos_ball[0] += int(vel_ball[0])
        pos_ball[1] += int(vel_ball[1])

        surface.fill(BLACK)

        pygame.draw.line(surface, WHITE, [WINDOW_WIDTH // 2, 0], [WINDOW_WIDTH // 2, 50], 1)
        pygame.draw.line(surface, WHITE, [WINDOW_WIDTH // 2,  75], [WINDOW_WIDTH // 2, 125], 1)
        pygame.draw.line(surface, WHITE, [WINDOW_WIDTH // 2, 150], [WINDOW_WIDTH // 2, 200], 1)
        pygame.draw.line(surface, WHITE, [WINDOW_WIDTH // 2, 225], [WINDOW_WIDTH // 2, 275], 1)
        pygame.draw.line(surface, WHITE, [WINDOW_WIDTH // 2, 300], [WINDOW_WIDTH // 2, 350], 1)
        pygame.draw.circle(surface, WHITE, pos_ball, 7)

        _player_score = font_arial.render("Player current score: " + str(PLAYER_SCORE), 1, GREEN)
        _player_game = font_arial.render("Total games won: " + str(PLAYER_GAMES_WON), 1, GREEN)
        _AI_score = font_arial.render("AI current score: " + str(AI_SCORE), 1, GREEN)
        _AI_game = font_arial.render("Total games won: " + str(AI_GAMES_WON), 1, GREEN)

        surface.blit(_player_score, (125, 440))
        surface.blit(_player_game, (125, 460))
        surface.blit(_AI_score, (525, 440))
        surface.blit(_AI_game, (525, 460))

        pos_paddle_four[1] = pos_ball[1]
        pos_paddle_five[0] = pos_ball[0]
        pos_paddle_six[0] = pos_ball[0]
        surface.blit(paddle_resize_one, paddle_one)
        surface.blit(paddle_resize_one, paddle_four)
        surface.blit(paddle_resize_two, paddle_two)
        surface.blit(paddle_resize_two, paddle_three)
        surface.blit(paddle_resize_two, paddle_five)
        surface.blit(paddle_resize_two, paddle_six)

        if 0 <= int(pos_paddle_four[1]) <= WINDOW_HEIGHT:
            paddle_four.centery = pos_ball[1]

        if int(pos_paddle_five[0]) >= WINDOW_WIDTH // 2 + 50:
            paddle_five.centerx = pos_ball[0]
            paddle_six.centerx = pos_ball[0]

        if int(pos_ball[0]) <= radius_ball + 10 and int(pos_ball[1]) in \
                range(pos_paddle_one[1], pos_paddle_one[1] + 100, 1):
            vel_ball[0] = -vel_ball[0]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[0]) >= 777 and int(pos_ball[1]) in range(pos_paddle_four[1], pos_paddle_four[1] + 100, 1):
            vel_ball[0] = -vel_ball[0]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[1]) <= radius_ball + 10 and int(pos_ball[0]) in range(paddle_two.left, paddle_two.right, 1):
            vel_ball[1] = -vel_ball[1]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[1]) >= WINDOW_HEIGHT - radius_ball - 10 and int(pos_ball[0]) in \
                range(paddle_three.left, paddle_three.right, 1):
            vel_ball[1] = -vel_ball[1]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[1]) <= 10 and int(pos_ball[0]) in range(paddle_five.left, paddle_five.right, 1):
            vel_ball[1] = -vel_ball[1]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[1]) >= 384 and int(pos_ball[0]) in range(paddle_six.left, paddle_six.right, 1):
            vel_ball[1] = -vel_ball[1]
            vel_ball[0] *= 1.1
            vel_ball[1] *= 1.1
            pong_collide_sound.play()

        if int(pos_ball[1]) < 0:
            if int(pos_ball[0]) >= WINDOW_WIDTH // 2:
                PLAYER_SCORE += 1
                point_scored_sound.play()
                MAX_SCORE_PLAYER -= 1
                break
            else:
                AI_SCORE += 1
                MAX_SCORE_AI -= 1
                point_scored_sound.play()
                break

        if int(pos_ball[0]) > WINDOW_WIDTH + radius_ball:
            PLAYER_SCORE += 1
            point_scored_sound.play()
            MAX_SCORE_PLAYER -= 1
            break

        if int(pos_ball[0]) < 0 - radius_ball:
            AI_SCORE += 1
            point_scored_sound.play()
            MAX_SCORE_AI -= 1
            break

        pygame.display.update()
        main_clock.tick(40)

    if AI_SCORE >= 11 and AI_SCORE > PLAYER_SCORE - 2:
        AI_GAMES_WON += 1
        AI_SCORE = 0
        PLAYER_SCORE = 0
        MAX_SCORE_AI = 11
        MAX_SCORE_PLAYER = 11
        game_lost_sound.play()
        if AI_GAMES_WON >= 3:
            pygame.mixer.music.play(-1, 0.0)
            game_lost = font_arial.render("GAME LOST! AI TOO GOOD!\nPress any button to play again.", 1, WHITE)
            surface.blit(game_lost, (200, 150))
            pygame.display.update()
            continue_game()
            pygame.mixer.music.stop()
            AI_GAMES_WON = 0
            PLAYER_GAMES_WON = 0
    if PLAYER_SCORE >= 11 and PLAYER_SCORE > AI_SCORE - 2:
        PLAYER_GAMES_WON += 1
        AI_SCORE = 0
        PLAYER_SCORE = 0
        MAX_SCORE_AI = 11
        MAX_SCORE_PLAYER = 11
        game_won_sound.play()
        if PLAYER_GAMES_WON >= 3:
            pygame.mixer.music.play(-1, 0.0)
            game_lost = font_arial.render("GAME WON! YOU ARE TOO GOOD!\nPress any button to play again.", 1, WHITE)
            winner_winner_player.play()
            surface.blit(game_lost, (200, 150))
            pygame.display.update()
            continue_game()
            pygame.mixer.music.stop()
            AI_GAMES_WON = 0
            PLAYER_GAMES_WON = 0

    pygame.display.update()

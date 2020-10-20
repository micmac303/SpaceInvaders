import math

import pygame

from pygame import mixer

# Initialise pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders-icon.png')
pygame.display.set_icon(icon)

# Initialise Player
player_img = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Initialise Enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []


def enemy_animation(number_of_rows, enemy_speed):
    y_position_offset = 0
    for z in range(number_of_rows):
        x_position_offset = 0
        for i in range(11):
            enemy_img.append(pygame.image.load('enemy.png'))
            enemyX.append(50 + x_position_offset)
            enemyY.append(60 + y_position_offset)
            enemyX_change.append(enemy_speed)
            enemyY_change.append(70)
            x_position_offset += 70
        y_position_offset += 70

    return 11 * number_of_rows


# Initialise Bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.8
bullet_state = 'ready'

# Prepare display text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_textX = 10
score_textY = 10


def display_game_over_text(game_over_text, text_x):
    loose_text = game_over_font.render(game_over_text, True, (255, 255, 255))
    screen.blit(loose_text, (text_x, 250))


def display_score_text(x, y):
    score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))


def draw_player(x, y):
    screen.blit(player_img, (x, y))


def draw_enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(eX, eY, bX, bY):
    distance = math.sqrt(math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2))
    if distance < 30:
        return True


# Game loop
num_of_enemies = enemy_animation(2, 0.6)
ended = True
running = True
while running:
    # RGB red, green, blue
    screen.fill((20, 10, 60))
    # loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If key pressed check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
                bulletX = playerX
                bullet_state = 'fire'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            if ended:
                game_over_sound = mixer.Sound('game_over_sound.wav')
                game_over_sound.play()
                game_over_speech = mixer.Sound('game_over_speech.wav')
                game_over_speech.play()
                ended = False
            screen.fill((230, 21, 21))
            display_game_over_text('GAME OVER', 200)
            break
        elif score_value == num_of_enemies:
            if ended:
                win_sound = mixer.Sound('win_sound.wav')
                win_sound.play()
                win_speech = mixer.Sound('win_speech.wav')
                win_speech.play()
                ended = False
            screen.fill((46, 232, 56))
            display_game_over_text('YOU WIN!', 245)
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 800:
            enemyX[i] = 0
            enemyY[i] += enemyY_change[i]

        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyY[i] = -1000

        draw_enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    draw_player(playerX, playerY)
    display_score_text(score_textX, score_textY)
    pygame.display.update()

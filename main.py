import pygame
import math

# Initialise pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders-icon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_img = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 60
enemyX_change = 0.1
enemyY_change = 50

# Bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.3
bullet_state = 'ready'

score = 0


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(eX, eY, bX, bY):
    distance = math.sqrt(math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2))
    if distance < 30:
        return True


# Game loop
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
                bulletX = playerX
                bullet_state = 'fire'
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX >= 800:
        enemyX = 0
        enemyY += enemyY_change

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = 370
        enemyY = 60

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

import pygame

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
enemyX_change = 0


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


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
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

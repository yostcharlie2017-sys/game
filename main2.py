# Tiny Roblox-Style Block Game in Python
# Requires: pygame
# Install with: pip install pygame

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Roblox Python")

clock = pygame.time.Clock()

# Colors
SKY = (120, 200, 255)
GRASS = (50, 200, 50)
DIRT = (120, 70, 20)
WHITE = (255, 255, 255)
RED = (255, 60, 60)
YELLOW = (255, 255, 0)

# Player
player = pygame.Rect(100, 100, 40, 60)
player_speed = 6
jump_power = -15
gravity = 0.8
velocity_y = 0
on_ground = False

# Blocks
blocks = []

for i in range(0, WIDTH, 50):
    blocks.append(pygame.Rect(i, HEIGHT - 50, 50, 50))

# Floating platforms
for i in range(12):
    x = random.randint(100, WIDTH - 100)
    y = random.randint(150, HEIGHT - 150)
    blocks.append(pygame.Rect(x, y, 100, 25))

# Coins
coins = []
for i in range(10):
    coins.append(pygame.Rect(
        random.randint(50, WIDTH - 50),
        random.randint(50, HEIGHT - 100),
        20,
        20
    ))

score = 0

font = pygame.font.SysFont(None, 40)

running = True
while running:
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= player_speed

    if keys[pygame.K_d]:
        player.x += player_speed

    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power

    # Gravity
    velocity_y += gravity
    player.y += velocity_y

    # Collision
    on_ground = False

    for block in blocks:
        if player.colliderect(block):
            if velocity_y > 0:
                player.bottom = block.top
                velocity_y = 0
                on_ground = True

    # Keep in screen
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    # Collect coins
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

    # Draw
    screen.fill(SKY)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, DIRT, block)
        pygame.draw.rect(screen, GRASS,
                         (block.x, block.y, block.width, 8))

    # Draw player
    pygame.draw.rect(screen, RED, player)

    # Eyes
    pygame.draw.circle(screen, WHITE, (player.x + 12, player.y + 18), 4)
    pygame.draw.circle(screen, WHITE, (player.x + 28, player.y + 18), 4)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin.center, 10)

    # Score
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (20, 20))

    # Win message
    if len(coins) == 0:
        win_text = font.render("YOU WIN!", True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - 100, 80))

    pygame.display.flip()

pygame.quit()
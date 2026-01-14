#Write a program to create a Space Invader Game using Pygame Library in Python.
import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500 
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
 
# Initialize Pygame
pygame.init()
running=True
# Create the screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Creating a background
background = pygame.image.load('bg.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bulletX_change = 0
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    


# Loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -15
            if event.key == pygame.K_RIGHT:
                playerX_change = 15

        if event.type == pygame.K_SPACE and bullet_state == "ready":
            print("bullet ready")
            bulletX = playerX
            fire_bullet(bulletX,bulletY)
            
           
            
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
        else:
            bullet_state = "fire"
            fire_bullet(bulletX, bulletY)
            bulletY = bulletY- bulletY_change    

        playerX = playerX + playerX_change
        screen.blit(playerImg, (playerX, playerY))
        pygame.display.update()
        
        



    

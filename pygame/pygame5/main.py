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
BULLET_SPEED_Y = 3.5
COLLISION_DISTANCE = 27
score_value = 0
 
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
    screen.blit(bulletImg, (x, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

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
                playerX = playerX + playerX_change  
            
            if event.key == pygame.K_SPACE and bullet_state=="ready":
               bulletX = playerX
               fire_bullet(bulletX,bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Update player position
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    if playerX > SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64
    
    # Game Over
    #Enemy Movement
    for i in range(num_of_enemies):
        
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            break
        enemyX[i]=enemyX[i]+enemyX_change[i]
        if enemyX[i] <=0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        screen.blit(enemyImg[i],(enemyX[i],enemyY[i]))
   

         
    # Bullet Movement        
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    else:
        bullet_state = "fire"
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change    

        
    screen.blit(playerImg, (playerX, playerY))
    pygame.display.update()
    pygame.display.set_caption(f"Space Invaders  Score: {score_value}")
pygame.quit()   
        
        



    

# Write a Python program to add one player
# and seven other enemy sprites (positioned randomly) 
# to the game screen. A variable score should have its
# values increased by one whenever the sprites collide.
import pygame
import random
# Initialize Pygame
pygame.init()
# Set up Screen
screen = pygame.display.set_mode((600, 400))
# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 200)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 570)
        self.rect.y = random.randint(0, 370)
# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
# Create player 
player = Player()
all_sprites.add(player)
# Create enemy sprites
for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
# Game variables
score = 0
clock = pygame.time.Clock()
running = True
# Main game loop
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update sprites
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    # Draw screen
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    if score == 50:
        running = False
        font.render("You Win!", True, GREEN)
        screen.blit(score_text, (250, 180))
pygame.quit()
#Write a Python program to create a Game screen and add two rectangular 
#sprites to it using the Pygame library. Add controls to one of the sprites 
#as well for up, down, left and right movements.
import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Screen with Movable Sprites")
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
all_sprites = pygame.sprite.Group()
player_sprite = RectangleSprite(100, 200, 50, 80, BLUE)  
enemy_sprite = RectangleSprite(600, 200, 50, 80, RED)    
all_sprites.add(player_sprite)
all_sprites.add(enemy_sprite)
SPEED = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_sprite.rect.x > 0:
        player_sprite.rect.x -= SPEED
    if keys[pygame.K_RIGHT] and player_sprite.rect.x < SCREEN_WIDTH - 50:
        player_sprite.rect.x += SPEED
    if keys[pygame.K_UP] and player_sprite.rect.y > 0:
        player_sprite.rect.y -= SPEED
    if keys[pygame.K_DOWN] and player_sprite.rect.y < SCREEN_HEIGHT - 80:
        player_sprite.rect.y += SPEED
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()
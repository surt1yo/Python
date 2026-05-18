#Write a program where a player controls a 
#sprite when two sprites collide , the game 
#displaying a win message upon meeting a specific condition.
import pygame
import random
done=False
MOVEMENT_SPEED=5
# Initialize Pygame
pygame.init()
# Background Image
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", 72)

# Class Sprite
class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        #Creating the Sprite image
        self.image=pygame.Surface((width,height))
        self.image.fill(colour)

        #Creating the rectangular object
        self.rect=self.image.get_rect()
    def move(self,newX,newY):
        self.rect.x=max(min(self.rect.x + newX, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y=max(min(self.rect.y + newY, SCREEN_HEIGHT - self.rect.height), 0)

bg_image=pygame.transform.scale(pygame.image.load("download.jpeg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collider")

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Group all the sprites together
all_sprites=pygame.sprite.Group()
s1=Sprite(pygame.Color("red"),20,30)
s1.rect.x=random.randint(0,SCREEN_WIDTH-s1.rect.width)
s1.rect.y=random.randint(0,SCREEN_HEIGHT-s1.rect.height)
all_sprites.add(s1)

s2=Sprite(pygame.Color("black"),20,30)
s2.rect.x=random.randint(0,SCREEN_WIDTH-s2.rect.width)
s2.rect.y=random.randint(0,SCREEN_HEIGHT-s2.rect.height)
all_sprites.add(s2)

won=False

# Keep the screen open
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True


    if not won:
       keys = pygame.key.get_pressed()
       x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
       y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
       s1.move(x_change, y_change)
       if s1.rect.colliderect(s2.rect):
           all_sprites.remove(s2)
           won = True

    screen.blit(bg_image,(0,0))  
    all_sprites.draw(screen)
      # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                           (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()  
        
pygame.quit()            
#Write a Python program to add two sprites and 
#create a custom event of changing the colour of the sprites.
import pygame
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Custom Sprite Event")
clock=pygame.time.Clock()
CHANGE_COLOR_EVENT=pygame.USEREVENT+1
pygame.time.set_timer(CHANGE_COLOR_EVENT,1000)
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self,color,width,height,pos):
        super().__init__()
        self.color=color
        self.image=pygame.Surface((width, height))
        self.image.fill(self.color)
        self.rect=self.image.get_rect(center=pos)
    def set_color(self,color):
        self.color=color
        self.image.fill(self.color)
sprite1=ColorSprite((255,0,0),80,80,(WIDTH//3,HEIGHT//2))
sprite2=ColorSprite((0,0,255),80,80,(2*WIDTH//3,HEIGHT//2))
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2) 
colors = [
    (255, 0, 0),    
    (0, 255, 0),    
    (0, 0, 255),    
    (255, 255, 0),  
]
color_index = 0
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == CHANGE_COLOR_EVENT:
            color_index = (color_index + 1) % len(colors)
            new_color = colors[color_index]
            sprite1.set_color(new_color)
            sprite2.set_color(new_color)
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()  

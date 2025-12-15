#Write a program that detects when keys are pressed and changes the 
#color of a sprite when it touches the screen boundaries.
import pygame
# Initialize Pygame
pygame.init()
done=False
# Making the gaming screen
screen=pygame.display.set_mode((500,400))
# Set the background color
bg_colour=(255,255,255)
# Detector
pygame.display.set_caption("Colour changing sprites")
colours={"red":pygame.Color('red'),
         "green":pygame.Color('green'),
         "blue":pygame.Color('blue'),
         "yellow":pygame.Color('yellow')}
start_colour=colours["red"]
x=40
y=40
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            x=x-10
        if key[pygame.K_RIGHT]:
            x=x+10
        if key[pygame.K_UP]:
            y=y-10
        if key[pygame.K_DOWN]:
            y=y+10
        if x==500-20 or x==0:
            start_colour=colours["blue"]
        if y==400-80 or y==0:
            start_colour=colours["green"]
        screen.fill(bg_colour)
        pygame.draw.rect(screen,start_colour,pygame.Rect(x,y,20,80))    
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
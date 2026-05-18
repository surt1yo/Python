#Write a Python program to create a Game screen and add elements like - 
#rectangle and text using the Pygame library.
import pygame
import random
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("My first game screen")
bg_color=(255,255,255)
rect_color=(0,125,255)
font_color=(0,0,0)
font=pygame.font.Font(None,74)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(bg_color)
    pygame.draw.rect(screen,rect_color,pygame.Rect(150,150,200,100))
    text=font.render("Hello Pygame!",True,font_color)
    screen.blit(text,(250,300))
    pygame.display.flip()
pygame.quit()

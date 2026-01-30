#Write a Python program to create an empty Pygame window.
import pygame
#Initialize Pygame
pygame.init()
#Creating the gaming window
screen=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
#Write a Python program to create your first Game screen using the Pygame library.
import pygame
# Initialize Pygame
pygame.init()
# Create the game window
screen=pygame.display.set_mode((500, 300))
image=pygame.image.load('bigguy.jpg')
bigguy_img=(pygame.transform.scale(image,(300,300)))
bg_color = (58,58,58)
screen.fill(bg_color)
screen.blit(bigguy_img,(100,0))
pygame.display.flip()

# Main loop to keep the window open
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
#Write a program to create a Pygame window with two circles, 
#one solid and another hollow circle with border width 
#3. Keep the background colour as - white RGB(255, 255, 255) 
#and the colour of the rectangle as green (0, 255, 0). 
#Try changing the values of centre and radius to see how the position and size of the balls change.
import pygame
# Initialize Pygame
pygame.init()
done=False
# Making the gaming screen
screen=pygame.display.set_mode((500,400))
# Set the background color
bg_colour=(255,255,255)
screen.fill(bg_colour)
# Circle Colours
pygame.draw.circle(screen,(0,255,0),(100,100),50)
pygame.draw.circle(screen,(0,0,255),(300,300),50,3)
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
pygame.quit()

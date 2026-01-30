#Write a program to create a Pygame window with a rectangle in it. 
#Keep the background colour as - black RGB(0,0,0) and color 
#of the rectangle as blue (0, 125, 255). Position the rectangle 
#anywhere on the screen. Try changing the values of top, left, 
#height and width to see how the position and size of the rectangle changes.
import pygame
done=False
# Initialize Pygame
pygame.init()
# Make tha gaming screen
screen=pygame.display.set_mode((500,400))
# Set the background color
bg_color=(0,0,0)
screen.fill(bg_color)
# Rectangle Colour
rect_color=(0,125,255)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        else:
            pygame.draw.rect(screen,rect_color,pygame.Rect(40,40,100,70))
            pygame.display.flip()
pygame.quit()    

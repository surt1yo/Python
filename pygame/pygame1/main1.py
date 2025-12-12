#Write a program to create a Pygame window with an image in it. 
#Use white colour as background RGB (255, 255, 255). 
#You can use any image of your choice.
import pygame
#Initialize Pygame
pygame.init()
#Creating the gaming window
screen=pygame.display.set_mode((400,300))
image=pygame.image.load('white.jpg')
bg=(pygame.transform.scale(image,(400,300)))
image=pygame.image.load('character.jpg')
image1=pygame.image.load('bigguy.jpg')
character_img=(pygame.transform.scale(image,(150,150)))
bigguy_img=(pygame.transform.scale(image1,(100,50)))
text=pygame.font.Font(None,36).render("Hello World",True,(pygame.Color('black')))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        else: 
            screen.blit(bg,(0,0))   
            screen.blit(character_img,(125,75))
            screen.blit(text,(130,20))
            screen.blit(bigguy_img,(250,200))
            pygame.display.flip()


pygame.quit()


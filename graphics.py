import pygame, random

def drawScene(window):
    # load in an image
    img = pygame.image.load("dude.gif")

    randPoint = (random.randint(0,500),random.randint(0,400))
    #draw the image on the screen
    window.blit(img,randPoint)

    pygame.draw.circle(window,(255,0,0),(random.randint(100,400),random.randint(0,300)),50)


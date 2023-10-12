# Using Libraries

# one useful library is:  random
import random

import pygame
import sys
from graphics import *

print(random.randint(2, 22))
# randint(a,b) gives a random integer between a and b, inclusive

print(random.random())
# generates a random number between 0.0 and 1.0

# pygame graphics notes
# create the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))

# set the screen to completely white
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
r = random.randint(0,256)
g = random.randint(0,256)
b = random.randint(0,256)
randColor = (r,g,b)
screen.fill(white)
red = (255, 0, 0)
green = (0, 125, 0)

# pygame.draw.rect(screen, green, (50,100,200,25), 4)
# pygame.draw.rect(screen,red,(50,100,80,60),7)
# pygame.draw.rect(screen, blue, (350,300,100,50), 5)
# pygame.draw.rect(screen, black, (250,200,50,100), 4)
# pygame.draw.rect(screen, blue, (150,300,100,50))
# pygame.draw.rect(screen, black, (450,200,50,100))
#
# point1=(200,200)
# point2 = (450,500)
# pygame.draw.line(screen, (randColor),point1,point2)
#
# pygame.draw.polygon(screen,green,(point1, (200,374),(85,250)),15)
#
drawScene(screen)


# update the display
pygame.display.update()

while (True):
    for event in pygame.event.get():
        # check if the user closed the window
        # you can quit either by clicking the RED [X] or by pressing the Esc key
        if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
            # end the program
            pygame.quit()
            sys.exit()

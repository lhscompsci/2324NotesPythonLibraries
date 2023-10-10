# Using Libraries

# one useful library is:  random
import random
import pygame, sys

print (random.randint(2,22))
# randint(a,b) gives a random integer between a and b, inclusive

print(random.random())
# generates a random number between 0.0 and 1.0

#pygame graphics notes
#create the screen
pygame.init()
screen = pygame.display.set_mode((800,600))

#set the screen to completely white
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
screen.fill(black)

#update the display
pygame.display.update()

while( True ):
    for event in pygame.event.get():
        #check if the user closed the window
        if( event.type== pygame.QUIT):
            #end the program
            pygame.quit()
            sys.exit()

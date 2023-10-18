import math

import pygame
import random


def drawScene(window):
    # load in an image
    img = pygame.image.load("dude.gif")

    randPoint = (random.randint(0, 500), random.randint(0, 400))
    # draw the image on the screen
    window.blit(img, randPoint)

    pygame.draw.circle(window, (255, 0, 0), (random.randint(100, 400), random.randint(0, 300)), 50)
    center = (300, 500)
    color = (100, 200, 0)
    radius = 75
    pygame.draw.circle(window, color, center, radius)

    green = (0, 255, 0)
    r1 = ((10, 10), (100, 100))
    pygame.draw.arc(window, green, r1, 0, math.pi / 2, 2)

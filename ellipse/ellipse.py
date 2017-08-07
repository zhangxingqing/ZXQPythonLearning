import pygame
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Ellipse')
width=4
x=300
y=250
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
    screen.fill((0,0,200))
    #draw a ellipse
    color=255,0,255
    width=0
    position=250,150,300,200
    pygame.draw.ellipse(screen,color,position,width)
    pygame.display.update()

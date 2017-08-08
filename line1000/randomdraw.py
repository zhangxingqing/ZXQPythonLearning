import pygame
import sys
import time
import random

pygame.init()
screencaption=pygame.display.set_caption('hello world')
screen=pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
for i in range(1000):
    drawcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    zhijing = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    width = random.randint(0,2)
    pygame.draw.line(screen, drawcolor, (top, left),(left,top),width)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

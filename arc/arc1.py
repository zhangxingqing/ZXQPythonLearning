import math
import pygame
import sys
from pygame.locals import  *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")
screen.fill((0,0,200))
    #draw the arc
color=255,0,255#颜色编码
position=200,150,200,200
start_angle=math.radians(0)
end_angle=math.radians(180)
pygame.draw.arc(screen,color,position,start_angle,end_angle)
pygame.display.update()
while True :
    for event in pygame.event.get():
        if event.type==QUIT:
           sys.exit()#退出程序 制造冲突







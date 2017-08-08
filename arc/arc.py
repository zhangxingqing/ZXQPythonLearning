import math,pygame, sys
import random
from pygame.locals import  *
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")
screen.fill((0,0,200))
screen.fill((0,0,200))
    #draw the arc
for i in range(10):
    drawcolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    top=random.randint (0,400)
    left=random.randint(0,500)
    rectwidth=random.randint(0,255)
    rectheight=random.randint (0,100)
    start_angle=math.radians(0)
    end_angle=math.radians(180)
pygame.draw.arc(screen,drawcolor,(top,left,rectwidth,rectheight),start_angle,end_angle)
pygame.display.flip()#屏幕刷新


while True :
    for event in pygame.event.get():
        if event.type==QUIT:
           sys.exit()#退出程序









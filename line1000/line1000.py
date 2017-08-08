import pygame
import sys
import random #导入随机函数
pygame.init()
screencaption=pygame.display.set_caption('Draw 1000 lines')
screen=pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])#用白色填充屏幕
for i in range(1000):#for循环，循环1000次。每循环一次，画一条线
    drawcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))#随机颜色
    top = random.randint(0, 500)
    left = random.randint(0, 500)
    width = random.randint(0,2)#随机线宽
    pygame.draw.line(screen, drawcolor, (top, left),(left,top),width)#随机线的起始坐标和结束坐标
pygame.display.flip()#更新显示以反映你的修改
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

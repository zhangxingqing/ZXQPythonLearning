import pygame
import sys
from pygame.locals import * #导入pygame中的所有常量
pygame.init() #初使化pygame
screen=pygame.display.set_mode((600,500))#获取对显示系统的访问 ，并创建一个窗口
pygame.display.set_caption('Drawing Ellipse')#创建窗口的标题
while True:#创建一个事件处理循环
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()#设置关闭按键
    for event in pygame.event.get():#编历pygame事件数组
        if event.type==QUIT:#如果点击esc按钮
            sys.exit()#退出程序
    screen.fill((0,0,200))#使用颜色 0，0，200来清除屏幕
    #draw a ellipse
    color=255,0,255
    position=250,150,300,200#矩形的开始坐标为（250，150），矩形的大小为长300，高 200
    width=1#椭圆线宽参数。如果线宽是0或省略，则填充
    pygame.draw.ellipse(screen,color,position,width)#绘制椭圆
    pygame.display.update()#屏幕刷新

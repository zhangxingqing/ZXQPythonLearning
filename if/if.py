
import turtle

def quadrilateral(length,width):
    x=number
    t = turtle.Pen()
    colors=['green','purple','yellow','blue']
    for number in range(100):
        t.pencolor(colors[number%4])
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(width)
        return

shape = raw_input('please enter a shape that you want to draw:')
number1 = input('please enter a number for  a length:')
number2 = input('please enter a number for a width:')
if shape=="rectangle":
    if number1>number2 or number1 <number2:
        print'You want to draw a rectangle!'
        print quadrilateral(number1, number2)
elif shape=='square' and number1==number2 :
    print 'You want to draw a square!'
    print quadrilateral(number1, number2)









































#def fibs(num):
  #  num=number
    #result=[0,1]
   # for i in range(num-2):
     #   result.append(result[-2]+result[-1])
    #return result
#for number in range(100000) :
  #  number = input('please enter a number:')
    #print fibs(number)

# import turtle
# t=turtle.Pen()
# for x in range(100):
#     t.forward(100)
#     t.left(90)
#     t.forward(150)
#     t.left(90)



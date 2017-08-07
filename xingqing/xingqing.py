import turtle

def quadrilateral(length,width):
    x=number
    t = turtle.Pen()
    colors=['green','purple','yellow','blue']
    t.pencolor(colors[x % 4])
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
        for number in range(100):
            print quadrilateral(number1, number2)
elif shape=='square' and number1==number2 :
    print 'You want to draw a square!'
    for number in range(100):
      print quadrilateral(number1, number2)























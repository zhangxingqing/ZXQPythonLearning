import turtle
t=turtle.Pen()
colors=['red','yellow','blue','green']
for x in range(100):
    t.pencolor(colors[x % 4])
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
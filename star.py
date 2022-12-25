import turtle
colors = ['red', 'pink', 'blue', 'light green', 'yellow','orange']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(150):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.right(108)
    t.backward(x)
    t.left(36)
turtle.done()    
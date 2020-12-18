import turtle
wn = turtle.getscreen()

wn.bgcolor('black')
colors = ['red','purple','blue','green','orange','yellow','pink']

draw = turtle.Turtle()
draw.pen(pencolor="purple",pensize=5)

#To draw multiple circle
# for x in range(10):
#     draw.pencolor(colors[x % len(colors)])
#     draw.circle(50)
#     draw.forward(x+5).
draw.fillcolor('red')
draw.begin_fill()


def drawshape():
    for i in range(200):
        draw.right(1)
        draw.forward(1)


draw.left(130)
draw.forward(127)
drawshape()

draw.left(130)
drawshape()
draw.forward(130)

draw.end_fill()
"""for x in range(100):
    draw.pencolor(colors[x % len(colors)])
    draw.pensize(30)"""

    #draw.width(x/100 + 1)
    #draw.forward(x)
    #draw.left(59)
turtle.done()
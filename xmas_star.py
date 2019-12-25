import turtle
import random
import time


def draw_circle(position):
    color = random.choice(colors)
    turtle.color('black', color)
    turtle.setposition(position)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()

def draw_xmas_tree():
    x = 0
    y = -200
    fd = 300
    # draw tree pot
    turtle.setposition(x+fd/3+20, y)
    turtle.color('forest green', 'forest green')
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

    # draw tree
    for i in range(3):
        turtle.setposition(x, y)
        turtle.pendown()
        turtle.begin_fill()
        for j in range(3):
            turtle.forward(fd)
            turtle.left(120)
        # store 6 positions for circle from each triangle.
        circle_positions.append((turtle.pos()[0]+fd/2, turtle.pos()[1]+90))
        circle_positions.append((turtle.pos()[0]+fd/2+40, turtle.pos()[1]+90))
        circle_positions.append((turtle.pos()[0]+fd/2-40, turtle.pos()[1]+90))
        circle_positions.append((turtle.pos()[0]+fd/2, turtle.pos()[1]+50))
        circle_positions.append((turtle.pos()[0]+fd/2+40, turtle.pos()[1]+50))
        circle_positions.append((turtle.pos()[0]+fd/2-40, turtle.pos()[1]+50))

        x += 20
        y += 90
        fd -= 40
        turtle.end_fill()
        turtle.penup()

def draw_xmas_star():
    turtle.color('black', 'yellow')
    turtle.penup()
    turtle.setposition(117, 198)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(72)
    turtle.forward(25)
    for i in range(4):
        turtle.right(144)
        turtle.forward(25)
        turtle.left(72)
        turtle.forward(25)
    turtle.end_fill()
    turtle.penup()

# arrays and variables
turtle.bgcolor("white")
colors = ["white", "red", "yellow", "blue"]
circle_positions = []

# start drawing
turtle.penup()
draw_xmas_tree()
draw_xmas_star()
for pos in circle_positions:
    draw_circle(pos)

turtle.done()

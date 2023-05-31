"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from base import vector
from base import line

ant = vector(0, 0)
aim = vector(2, 0)

def wrap(value):
    "Wrap value around -200 and 200."
    if value > 200:
        value = -200
    elif value < -200:
        value = 200
    return value  # TODO

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    #clear()
    goto(ant.x, ant.y)
    color = ''
    if (int(ant.x) > 0 and int(ant.y) > 0):
        color = 'blue'
    elif (int(ant.x) > 0 and int(ant.y) < 0):
        color = 'green'
    elif (int(ant.x) < 0 and int(ant.y) < 0):
        color = 'yellow'
    else:
        color = 'red'
    dot(10, color)


    if running:
        ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()

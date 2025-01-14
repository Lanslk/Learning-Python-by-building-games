"""Snake, classic arcade game.

Excercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from base import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Pen
pen = Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.goto(0, 150)
pen.write("Score : 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()


def change(x, y):
    "Change snake direction."
    if aim + vector(x, y) == vector(0, 0):
        return
    else:
        aim.x = x
        aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    if head.x < -200:
        head.x = 190
    elif head.x > 190:
        head.x = -200
    elif head.y < -200:
        head.y = 190
    elif head.y > 190:
        head.y = -200
    update()

    snake.append(head)

    if head == food:
        # print('Snake:', len(snake))
        pen.clear()
        pen.write("Score : {}".format(len(snake) - 1), align='center', font=('Courier', 24, 'bold'))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)  # snake speed


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

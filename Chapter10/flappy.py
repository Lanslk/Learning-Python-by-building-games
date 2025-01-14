"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from base import vector

bird = vector(0, 0)
balls = []
score = 0


def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    "Draw screen objects."
    clear()

    s = vector(-20, 190)
    goto(s.x, s.y)
    global score
    write("Score:%d" % score, False, align='left', font=("Arial", 16, "normal"))

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')  # ball size

    update()


def move():
    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    global score
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    for ball in balls:
        if ball.x == 0 or ball.x == -1 or ball.x == -2:
            score += 1

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            print(abs(ball - bird))
            draw(False)
            return

    draw(True)
    ontimer(move, 50)  # speed


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
# onscreenclick(tap)
listen()
onkey(lambda: bird.move(vector(0, 30)), 'Up')
onkey(lambda: bird.move(vector(30, 0)), 'Right')
onkey(lambda: bird.move(vector(-30, 0)), 'Left')
onkey(lambda: bird.move(vector(0, -30)), 'Down')
move()
done()

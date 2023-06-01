import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('blue')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(5, 1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 2.5
ball.dy = 2.5

# Ball1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape('circle')
ball1.color('white')
ball1.penup()
ball1.dx = 1.5
ball1.dy = 1.5

balls = (ball, ball1)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

# Score
score_a = 0
score_b = 0


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
def doMove():
    for ball in balls:
        global score_a
        global score_b
        # Moving Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center',
                      font=('Courier', 24, 'bold'))
            ball.color('white')

        if ball.xcor() < -390:
            ball.goto(0, 0)

            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center',
                      font=('Courier', 24, 'bold'))
            ball.color('white')

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (
                ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
            ball.color('red')
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (
                ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
            ball.color('blue')
            ball.setx(-340)
            ball.dx *= -1


while True:
    wn.update()

    doMove()

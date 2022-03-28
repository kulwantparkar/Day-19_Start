from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def forward():
    tom.forward(20)


def backward():
    tom.backward(20)


def clear():
    tom.home()
    tom.clear()


def left():
    current_heading = tom.heading() + 10
    tom.setheading(current_heading)


def right():
    current_heading = tom.heading() - 10
    tom.setheading(current_heading)


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)
# screen.onkey(key="Down", fun=down_direction)
screen.exitonclick()
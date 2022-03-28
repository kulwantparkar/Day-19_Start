import turtle
import  random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user = screen.textinput(title="Bet on Turtle", prompt="Choose a color:")


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_axis = [-150, -100, -50, 0, 50, 100, 150]

all_turtle = []
for turtles in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtles])
    new_turtle.goto(x=-230, y=y_axis[turtles])
    all_turtle.append(new_turtle)


if user:
    is_race_on = True

while is_race_on:

    for turtlee in all_turtle:
        if turtlee.xcor() > 230:
            is_race_on = False
            winning_color = turtlee.pencolor()
            if user == winning_color:
                print(f"You won! Your {winning_color} turtle won.")
            else:
                print(f"You lost! Your {winning_color} turtle lost. ")



        rand_num = random.randint(0, 10)
        turtlee.forward(rand_num)











screen.exitonclick()

# jerry = Turtle(shape="turtle")
# ben = Turtle(shape="turtle")
# nick = Turtle(shape="turtle")
# mac = Turtle(shape="turtle")
# om = Turtle(shape="turtle")
# sonu = Turtle(shape="turtle")
#
#
# tom.penup()
# jerry.penup()
# ben.penup()
# nick.penup()
# mac.penup()
# om.penup()
# sonu.penup()
#
# tom.color("red")
# jerry.color("orange")
# ben.color("yellow")
# nick.color("green")
# mac.color("blue")
# om.color("indigo")
# sonu.color("violet")
#
#
# tom.goto(x=-230, y=150)
# jerry.goto(x=-230, y=100)
# ben.goto(x=-230, y=50)
# nick.goto(x=-230, y=0)
# mac.goto(x=-230, y=-50)
# om.goto(x=-230, y=-100)
# sonu.goto(x=-230, y=-150)
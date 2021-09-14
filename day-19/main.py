import secrets
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

height = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=height)
    height += 40
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You've won! The winner is {winner_color}.")
            else:
                print(f"You've lost! The winner is {winner_color}.")
        turtle.forward(secrets.choice(range(0, 11)))

screen.exitonclick()

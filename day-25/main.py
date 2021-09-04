import turtle

import pandas

FONT = ("Courier", 12, "bold")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
x_coordinates = data.x.to_list()
y_coordinates = data.y.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in data.state.to_list() and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(answer_state, font=FONT)
        guessed_states.append(answer_state)

    elif answer_state == "Exit":
        states_to_learn = []

        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

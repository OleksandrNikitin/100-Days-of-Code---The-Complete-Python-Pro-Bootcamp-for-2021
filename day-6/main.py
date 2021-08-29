def at_goal():
    pass


def turn_left():
    pass


def front_is_clear():
    pass


def move():
    pass


def right_is_clear():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def infinite_move():
    while front_is_clear() and not at_goal():
        move()
        if right_is_clear():
            break


while not at_goal():
    infinite_move()
    if right_is_clear():
        turn_right()
        if front_is_clear() and not at_goal():
            infinite_move()
    else:
        turn_left()

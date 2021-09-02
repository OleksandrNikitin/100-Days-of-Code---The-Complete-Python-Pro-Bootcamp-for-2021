from turtle import Turtle

WIDTH = 5
HEIGHT = 1
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.goto(x=self.x_pos, y=self.y_pos)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(x=self.x_pos, y=new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(x=self.x_pos, y=new_y)

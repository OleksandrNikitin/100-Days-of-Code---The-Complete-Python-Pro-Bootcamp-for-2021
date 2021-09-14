import secrets
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = secrets.choice(range(-280, 281))
        random_y = secrets.choice(range(-280, 281))
        self.goto(random_x, random_y)

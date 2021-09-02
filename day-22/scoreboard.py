from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.left_score} - {self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.clear()
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.clear()
        self.right_score += 1
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

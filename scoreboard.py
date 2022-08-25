from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_left = 0
        self.paddle_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.redraw()

    def redraw(self):
        self.clear()
        self.write(f"SCORE {self.paddle_left} : {self.paddle_right}", align=ALIGNMENT, font=FONT)

    def score_left(self):
        self.paddle_left += 1
        self.redraw()

    def score_right(self):
        self.paddle_right += 1
        self.redraw()

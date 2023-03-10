from turtle import Turtle
ALIGN = "left"
FONT = ("Arial", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)

    def count_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align= ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game OVer', move=False, align= ALIGN, font=FONT)

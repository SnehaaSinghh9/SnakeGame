from turtle import Turtle
from snake import Snake
ALIGN = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        # self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.points}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"    Oops!\nGame Over! :(\nYour Score = {self.points}", align=ALIGN, font=FONT)

    def score(self):
        self.points += 1
        # self.score += 1
        self.clear()
        self.update_scoreboard()




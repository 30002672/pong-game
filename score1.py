import time
from turtle import Turtle

# for paddle on the left
class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        #self.position = position
        self.goto(position)

        self.penup()
        self.color("white")

        self.score_num = -1

        #self.write(f"Score: {self.score_num}", align="center", font=("Courier", 18, "normal"))
        #self.color("black")

    def score_update(self):
        self.color("white")
        self.clear()

        self.score_num+=1
        self.write(f"Score: {self.score_num}", align="center", font=("Courier", 18, "normal"))
        self.color("black")

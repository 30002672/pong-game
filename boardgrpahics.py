from turtle import Turtle, Screen
import time


# for paddle on the left
class board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.setheading(270)
        self.speed("fastest")
        self.score_num = 0

    def line(self):

        list = []
        while self.ycor() >-300:
            self.width(5)
            self.forward(25)
            self.penup()
            self.forward(25)
            self.pendown()


    def disappear(self):
        self.color("black")






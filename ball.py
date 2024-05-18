from turtle import Turtle, Screen
import time
from paddles import Pad
screen = Screen()


class ball(Turtle):
    def __init__(self):
        super().__init__()


        self.new_x = None
        self.shape("circle")
        self.color("white")
        self.shapesize(0.8, 0.8)
        self.goto(0, 0)
        self.penup()
    #
        self.new_x = 5
        self.new_y = 2.5

    def move(self):
        self.speed(1)

        self.newx2 = self.xcor() + self.new_x
        self.newy2 = self.ycor() + self.new_y
        self.goto(self.newx2, self.newy2)
    #def bounce(self):

        # y coordinate changes when collosion is on the top and bottom walls
        if self.ycor() >= 296:
            self.new_y*=-1
        elif self.ycor() <= -296:
            self.new_y *= -1

    def pad_detect(self):# x coordnate changes when the collosion is on the paddle
        self.new_x*=-1

    def restart(self):
        time.sleep(3)
        self.goto(0,0)





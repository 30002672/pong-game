#main file
# CREATING THE SCOREBOARD ( LINE AND SOCRE KEEPER)
# PADDLES/ BALL FILE

from turtle import Turtle,Screen
from paddles import Pad
from ball import ball
from boardgrpahics import board
from score1 import Score

import time



paddle = Pad((-290,0))
paddle2= Pad((290,0))
board = board()

score = Score((-180,250))
score2 = Score((180,250))

score.score_update()
score2.score_update()
board.line()
board.disappear()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

#screen.tracer(0)
ball = ball()



screen.onkeypress(paddle2.down, "Down")
screen.onkey(paddle2.release_key, "Down")

screen.onkeypress(paddle2.up, "Up")
screen.onkey(paddle2.release_key, "Up")


screen.onkeypress(paddle.down, "s")
screen.onkey(paddle.release_key, "s")

screen.onkeypress(paddle.up, "w")
screen.onkey(paddle.release_key, "w")

screen.listen()



bol = True
i = 0
while i < 5:
    if ball.distance(paddle2.pos()) < 35:
        ball.pad_detect()
    elif ball.distance(paddle.pos()) <35:
        ball.pad_detect()
    elif abs(ball.xcor()) >290:
        bol = False
        i+=1


        if ball.distance(paddle.pos()) < ball.distance(paddle2.pos()):
            score2.score_update()
        else:
            score.score_update()
        bol = True

        ball.restart()

    ball.move()


    #if ball.ycor() >= 300:
    #ball.bounce()

    screen.update()

#screen.onkey(paddle.up, "Up")
#screen.onkey(paddle.down, "Down")


screen.exitonclick()




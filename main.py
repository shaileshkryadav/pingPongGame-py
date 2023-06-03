from turtle import Screen
from pingPong import Ping
from ball import Ball
import time
from ScoreBoard import Board

r_paddle = Ping(350, 0)
l_paddle = Ping(-350, 0)
ball = Ball()
score = Board()



game_is_on = True





screen = Screen()
screen.listen()
screen.tracer()
screen.setup(width=800, height=600)
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.listen()
screen.bgcolor('black')
screen.title('PingPong')

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    bounce=True
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(l_paddle)<70 and ball.xcor()<-320 or ball.distance(r_paddle)<60 and ball.xcor()<320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_ball()
        score.score_x2()



    if ball.xcor() < -380:
        ball.reset_ball()
        score.score_x1()
    score.refresh_Score()






screen.exitonclick()

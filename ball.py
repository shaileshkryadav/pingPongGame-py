from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.goto(0, 0)
        self.x = 10
        self.y = 10
        self.move_speed=0.2


    def move(self):
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x, y)

    def bounce(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.5

    def reset_ball(self):
        self.speed(0.2)
        self.move_speed = 0.2
        self.goto(0,0)
        self.bounce_x()



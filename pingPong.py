from turtle import Turtle


class Ping(Turtle):

    def __init__(self,x_position, y_position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(x_position,y_position)


    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


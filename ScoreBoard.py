from turtle import Turtle

class Board(Turtle):


    def   __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto( 0, 260)
        self.write(f'{self.score_l } || {self.score_r}', move=False, align='center', font=('Arial', 20, 'normal'))


    def score_x1(self):
        self.score_r+= 1
        self.clear()


    def score_x2(self):
        self.score_l += 1
        self.clear()



    def refresh_Score(self):
        self.write(f'{self.score_l } || {self.score_r}', move=False, align='center', font=('Arial', 20, 'normal'))
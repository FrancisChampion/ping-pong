from turtle import Turtle

class score_board(Turtle):


    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup() 
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.update_score() # calling the function below to initialise the itself on the score_board
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_paddle_score, align = 'center', font = ('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_paddle_score, align = 'center', font = ('Courier', 80, 'normal'))


    def left_side_score(self):
        self.left_paddle_score += 1
        self.update_score()


    def right_side_score(self):
        self.right_paddle_score += 1
        self.update_score()
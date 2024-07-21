from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from score import score_board
#creating the board or screen on which the game will be played
game_board = Screen()
game_board.tracer(0) # stops the animation or movement of the paddle when the screen appears
game_board.bgcolor('white')
game_board.setup(width=900, height = 600) # dimension of the screen
game_board.title('Pong Game')

# creating the paddles with the Paddle class 
right_paddle = Paddle((400,0))
left_paddle = Paddle((-400,0))


ball = Ball()   #calling the ball class

score_record = score_board()  # calling the score_board class


#getting the paddles move by pressing the keys on the keyboard
# the right paddle moves up by the 'Up' navigation key and moves down by the 'Down' navigation key
# the left paddle moves up by lowercase letter 'a' and moves down by lowercase letter 'd'  
game_board.listen()
game_board.onkey(right_paddle.go_up, 'Up')
game_board.onkey(right_paddle.go_down,'Down')
game_board.onkey(left_paddle.go_up, 'a')
game_board.onkey(left_paddle.go_down,'d')



#getting the game played continues by updating the screen
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # To make sure the ball moves at a reasonable speed
    game_board.update()
    ball.move()
    #getting the ball bounce back after hitting the top and the bottom of the screen
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
        #getting the ball bounce back after colliding with the paddles

    if ball.distance(right_paddle) < 40 and ball.xcor() > 380 or ball.distance(left_paddle)<40 and ball.xcor()<-380:
        ball.bounce_x()


# if the right paddle misses the ball
    if ball.xcor() > 440:
        ball.start_all_over()
        score_record.left_side_score()
#if the left paddle misses the ball
    if ball.xcor() < -440:
        ball.start_all_over()
        score_record.right_side_score() 
    



from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

# Create a screen with background color black and of dimension 600(height) x 800(width)
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create two paddles, one left and one right.
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
score = Score()

# Start the screen to listen for the keys.
screen.listen()

# The right paddle player should use Arrow Up and Arrow Down key to move the paddle Up and Down.
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

# The left paddle player should use 'U' and 'D' key to move the paddle Up and Down.
screen.onkey(left_paddle.paddle_up, "u")
screen.onkey(left_paddle.paddle_down, "d")

# Start the game using while loop.
game_on = False

while not game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.refresh_ball()

    # Detect collision with the wall. We only consider the Y-axis (height) here because X-axis contains the paddles.

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with the paddles. We consider the X-axis to measure the distance between the paddle and ball.

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 \
            and ball.xcor() < -320:
        ball.x_bounce()

    # Check if the ball has gone past the paddle. If yes, reset the game and the opponent scores.
    # The ball should go to the opponent after resetting the game.

    if ball.xcor() > 390:
        ball.ball_reset()
        score.left_player_score()

    if ball.xcor() < -390:
        ball.ball_reset()
        score.right_player_score()

    # The game should get over when one of the player reaches 10. Call Game over function from Score class.
    if score.right_score >= 10 or score.left_score >= 10:
        game_on = True
        score.game_over()

screen.exitonclick()

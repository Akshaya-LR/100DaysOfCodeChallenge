# Import the Turtle and Random modules
# Import the snake.py, food.py and score.py

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# Initialize the Screen object and setup the screen to 600x600 and background color to Black

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
# Set the Screen tracer to zero, which turns off the animation until update is called.
screen.tracer(0)

# Initialize the snake, food, score objects
snake = Snake()
food = Food()
score = Score()

# Start the Screen listen event.
# Press Arrow Up to move UP and Arrow Down to move Down
# Press Arrow Right to move Right and Arrow Left to move Left
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Start the while loop until the game gets over.
game_on = False
while not game_on:
    # Call the Screen update() to turn on the animation.
    screen.update()
    time.sleep(0.1)
    # Call move() from snake module and use the arrow keys to control the snake on the screen.
    snake.move()

    # Check if the snake hit the food. If it hits, set a new food randomly on the screen. Also, extend the snake body
    # and increment the score.
    if snake.head_of_snake.distance(food) < 15:
        food.refresh_food()
        snake.extend_body()
        score.add_score()

    # Check if the snake hit any sides of the wall. If it hits, make the while loop stop.
    # It should display Game Over on the screen.
    if snake.head_of_snake.xcor() > 290 or snake.head_of_snake.xcor() < -290 or snake.head_of_snake.ycor() > 290 \
            or snake.head_of_snake.ycor() < -290:
        game_on = True
        score.game_over()

    # Check if the snake hit any segment of it's own body. If it hits, make the while loop stop.
    # It should display Game Over on the screen.
    for snakes in snake.my_snake[1:]:
        if snake.head_of_snake.distance(snakes) < 10:
            game_on = True
            score.game_over()

screen.exitonclick()

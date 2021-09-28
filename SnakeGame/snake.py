from turtle import Turtle

# Initialize constants
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Create the class Snake
class Snake:

    def __init__(self):
        self.my_snake = []
        for position in POSITIONS:
            self.add_segment(position)

        self.head_of_snake = self.my_snake[0]

    # Add body of the snake.
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.shapesize(stretch_wid=0.8, stretch_len=0.8)
        snake.penup()
        snake.goto(position)
        self.my_snake.append(snake)

    # When the snake hits the food, extend it's body using this function.
    def extend_body(self):
        self.add_segment(self.my_snake[-1].position())

    # Moving and controlling the snake using the belo functions.
    def move(self):
        for segment in range(len(self.my_snake) - 1, 0, -1):
            x_pos = self.my_snake[segment - 1].xcor()
            y_pos = self.my_snake[segment - 1].ycor()
            self.my_snake[segment].goto(x_pos, y_pos)
        self.my_snake[0].forward(DISTANCE)

    def up(self):
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def down(self):
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)

    def left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)

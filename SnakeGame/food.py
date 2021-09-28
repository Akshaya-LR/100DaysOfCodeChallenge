from turtle import Turtle
from random import randint


# Create a class Food which is a child of Turtle class.
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh_food()

    # Generate a new food randomly on the screen.
    def refresh_food(self):
        new_x_pos = randint(-280, 280)
        new_y_pos = randint(-280, 280)
        self.goto(new_x_pos, new_y_pos)

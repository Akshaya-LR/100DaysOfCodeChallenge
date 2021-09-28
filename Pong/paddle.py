from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_cor = x_pos
        self.y_cor = y_pos
        self.create_paddle(self.x_cor, self.y_cor)

    def create_paddle(self, x_position, y_position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)

    def paddle_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def paddle_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

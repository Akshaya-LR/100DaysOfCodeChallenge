from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_val = 10
        self.y_val = 10
        self.ball_speed = 0.1

    def refresh_ball(self):
        new_x_pos = self.xcor() + self.x_val
        new_y_pos = self.ycor() + self.y_val
        self.goto(new_x_pos, new_y_pos)

    def y_bounce(self):
        self.y_val *= -1

    def x_bounce(self):
        self.x_val *= -1
        self.ball_speed *= 0.8

    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_val *= -1

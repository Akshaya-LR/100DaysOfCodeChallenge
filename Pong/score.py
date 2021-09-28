from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"{self.left_score}", align="center", font=("Times new Roman", 35, "bold"))
        self.goto(150, 200)
        self.write(f"{self.right_score}", align="center", font=("Times new Roman", 35, "bold"))

    def left_player_score(self):
        self.left_score += 1
        self.score_update()

    def right_player_score(self):
        self.right_score += 1
        self.score_update()

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Times new Roman", 40, "bold"))

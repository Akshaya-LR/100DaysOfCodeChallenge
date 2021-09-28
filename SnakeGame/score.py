from turtle import Turtle


# Create a class Score which is a child of Turtle class.
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align="center", font=("Times new Roman", 15, "bold"))

    # Increment the score by 1 and update it to the scoreboard whenever the snake hits it's food.
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # Game over function when the snake hits the wall or it's body.
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Calibre", 20, "bold"))

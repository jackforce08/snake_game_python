from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
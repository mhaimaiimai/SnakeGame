from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0,280)
        self.pencolor("white")
        with open("highscore.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align="center", font = ("Arial", 14, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.setposition(0,0)
        self.write(f"GAME OVER", False, align="center", font = ("Arial", 24, "normal"))
from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0,280)
        self.pencolor("white")
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", False, align="center", font = ("Arial", 14, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.setposition(0,0)
        self.write(f"GAME OVER", False, align="center", font = ("Arial", 24, "normal"))
from turtle import *

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0

    def update_score(self):
        self.goto(-100,200)
        self.write(self.l_score,"centre",font=("Courier",80,"bold"))
        self.goto(100,200)
        self.write(self.r_score,"centre",font=("Courier",80,"bold"))

    def r_increment(self):
        self.r_score+=1
        self.clear()
    
    def l_increment(self):
        self.l_score+=1
        self.clear()

        


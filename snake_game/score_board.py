from turtle import *


        



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("data.txt","r") as data:
            self.high_score=data.read()
        self.penup()
        self.goto(x=0,y=260)
        self.hideturtle()
        self.score=0
        self.updatescore()
        
        

    def updatescore(self):
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}",align="center",font=('arial',24,'normal'))

    # def gameover(self):
    #     self.goto(x=0,y=0)
    #     self.write(f"GAME OVER",align="center",font=('arial',24,'normal'))

    def reset(self):
        if str(self.score)>self.high_score:
            self.high_score=str(self.score)
            with open('data.txt','w') as data:
                data.write(str(self.score))
        self.clear()
        self.score=0
        self.updatescore()

    def increase(self):
        self.score+=1
        self.clear()
        self.updatescore()
       

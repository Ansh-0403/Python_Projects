from turtle import *

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_xmove=10
        self.new_ymove=10

    def move(self):
        new_x=self.xcor()+self.new_xmove
        new_y=self.ycor()+self.new_ymove
        self.goto(x=new_x,y=new_y)

    def bounce(self):
        self.new_ymove*=-1
    
    def reflect(self):
        self.new_xmove*=-1

    def reset(self):
        self.home()
        self.reflect()

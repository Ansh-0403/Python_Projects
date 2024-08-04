from turtle import *

class game_paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=4)
        self.penup()
        self.goto(position)

    def up(self):
        new_y=self.ycor()+40
        new_x=self.xcor()
        self.goto(x=new_x,y=new_y)

    def down(self):
        new_x=self.xcor()
        new_y=self.ycor()-40
        self.goto(x=new_x,y=new_y)
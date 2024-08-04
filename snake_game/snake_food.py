from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x=random.randint(-290,290)
        rand_y=random.randint(-290,290)
        self.goto(x=rand_x,y=rand_y)

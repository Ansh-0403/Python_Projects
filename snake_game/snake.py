from turtle import *
import time
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVING_DISTANCE=20


class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.up()
        self.down()
        self.left()
        self.right()

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()


    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)
            
    def add_segment(self,position):
        segm=Turtle("square")
        segm.color("white")
        segm.penup()
        segm.goto(position)
        self.segments.append(segm)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
         for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
    
         self.segments[0].forward(MOVING_DISTANCE)
    
    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)







# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("SNAKE GAME")
# screen.tracer(0)
# x_cor,y_cor=0,0
# all_segments=[]

# game_dif=screen.textinput(title="easy=E,medium=M,difficult=D)",prompt="select your speed")

# if game_dif=="E":
#     time_dur=0.3
# elif game_dif=="M":
#     time_dur=0.1
# else:
#     time_dur=0.05


# for i in range(3):
#     segment_1=Turtle('square')
#     segment_1.color("white")
#     segment_1.penup()
#     all_segments.append(segment_1)

# for i in all_segments:
#     i.goto(x=x_cor,y=y_cor)
#     x_cor+=-20


# game_is_on=True

# while game_is_on:
#     screen.update()
#     time.sleep(time_dur)
    
#     for seg in range(len(all_segments)-1,0,-1):
#         new_x=all_segments[seg-1].xcor()
#         new_y=all_segments[seg-1].ycor()
#         all_segments[seg].goto(new_x,new_y)
    
#     all_segments[0].forward(20)
#     all_segments[0].left(90)
    



# screen.exitonclick()
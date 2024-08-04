from turtle import *
import time
from paddle import game_paddle
from ball import Ball
from score import Scoreboard

tim=Turtle()
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
dif=screen.textinput(title="Difficulty",prompt="Select your difficulty")
score=Scoreboard()


def whole_game():
    r_paddle=game_paddle((370,0))
    l_paddle=game_paddle((-370,0))
    pong_ball=Ball()

    screen.listen()
    screen.onkey(r_paddle.up,"Up")
    screen.onkey(r_paddle.down,"Down")
    screen.onkey(l_paddle.up,"w")
    screen.onkey(l_paddle.down,"s")

    game_is_on=True
    while game_is_on:
        score.update_score()
        screen.update()
        time.sleep(tim_dur)
        pong_ball.move()

        #detecting collision with upper and lower wall
        if pong_ball.ycor()>280 or pong_ball.ycor()<-280:
            pong_ball.bounce()

        #detect collision with paddle
        elif (l_paddle.distance(pong_ball)<40 and pong_ball.xcor()<-340) or (r_paddle.distance(pong_ball)<40 and pong_ball.xcor()>340):
            pong_ball.reflect()

        if pong_ball.xcor()>390:
            pong_ball.reset()
            score.l_increment()
            score.update_score()
            if score.l_score==5:
                tim.hideturtle()
                tim.color("blue")
                tim.goto(x=-80,y=-20)
                tim.write("LEFT WINS","center",font=("Courier",40,"normal"))
                game_is_on=False

        elif pong_ball.xcor()<-390:     
            pong_ball.reset()
            score.r_increment()
            score.update_score()
            if score.r_score==5:
                tim.hideturtle()
                tim.color("blue")
                tim.goto(x=-80,y=-20)
                tim.write("LEFT WINS","center",font=("Courier",40,"normal"))
                game_is_on=False
        

    screen.exitonclick()

#setting difficulty
if dif=="E":
    tim_dur=0.1
    whole_game()

elif dif=="M":
    tim_dur=0.05
    whole_game()

elif dif=="D":
    tim_dur=0.025
    whole_game()

else:
    print("select between E M or D")


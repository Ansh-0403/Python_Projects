from snake import Snake
import time
from turtle import *
from snake_food import Food
from score_board import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
food=Food()
scoreboard=Scoreboard()

game_dif=screen.textinput(title="easy=E,medium=M,difficult=D)",prompt="select your speed")

if game_dif=="E":
    time_dur=0.3
elif game_dif=="M":
    time_dur=0.1
else:
    time_dur=0.05

snake=Snake()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(time_dur)
    snake.move()

    #detect collison with food
    if snake.segments[0].distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    #collision with the wall
    if snake.segments[0].xcor()>290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290 or snake.segments[0].xcor()<-290:
        scoreboard.reset()
        snake.reset()

    #detect collision with the tail
    for i in snake.segments:
        if i==snake.head or i==snake.segments[1] or i==snake.segments[2]:
            pass
        else:
            if i.distance(snake.head)<20:
                scoreboard.reset()
                snake.reset()




screen.exitonclick()
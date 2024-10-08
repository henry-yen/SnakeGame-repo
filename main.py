#import
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


#create a black screen with size of 600X600 and with a title
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
#make it move
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Check the collision of the snake and the food
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.add()
        snake.add_segment()
    # Detect collision with wall
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False

    #Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on = False
#click on exit
screen.exitonclick()

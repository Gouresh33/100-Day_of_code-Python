from turtle import Screen
from food import Food
from scoreboard import *
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_position = [(0,0),(-20,0),(-40,0)]
segments = []


snake = Snake()
food = Food()
score = scoreboared()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.incre_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
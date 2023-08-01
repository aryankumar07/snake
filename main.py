from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_Score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset_score()
            snake.reset()


screen.exitonclick()
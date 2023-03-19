from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)
tim = Turtle("square")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collision with Food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score()

    # Detecting Collision with Wall
    x1 = snake.segments[0].xcor()
    y1 = snake.segments[0].ycor()
    if (x1 > 295) or (x1 < -295) or (y1 > 295) or (y1 < -295):
        game_is_on = False
        print("Game Over!")
        scoreboard.game_over()

    # Detecting Collision with Tail
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass
        # elif snake.segments[0].distance(segment)<10:
        #     game_is_on = False
        #     print("Game Over!")
        #     scoreboard.game_over()
        if snake.segments[0].distance(segment)<10:
            game_is_on = False
            print("Game Over!")
            scoreboard.game_over()


scr.exitonclick()
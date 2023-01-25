import time
from turtle import Screen
from snake import Snake
from food import Food
from points import Board

#Screen setup
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600,600)
screen.tracer(0)
screen.listen()

#Classes
snake = Snake()
food = Food()
board = Board()

#Calling movements
screen.onkey(snake.moveup,"Up")
screen.onkey(snake.movedown,"Down")
screen.onkey(snake.moveright,"Right")
screen.onkey(snake.moveleft,"Left")

#While the game is running
game_on = True
while game_on:
    screen.update()
    time.sleep(0.04)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        board.increase()
        snake.extend()

    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        game_on = False
        board.wallhit()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            game_on = False
            board.wallhit()


screen.exitonclick()
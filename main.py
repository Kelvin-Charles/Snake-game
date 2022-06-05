#Importation of modules
from turtle import Screen
from snake import Snake
import time


#declaring object from the Screen function in  turtle module
screen = Screen()

#Widget dimension,color and title
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Kelvin Snake Game")
screen.tracer(0)

#declaring object from the Snake function in  snake module
snake = Snake()

#declaring object from the Food function in  snake module
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()

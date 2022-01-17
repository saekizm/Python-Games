from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    
    #detect collision with the walls
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_on = False
        score.game_over()

    
    #detect collision with tail
    for seg in snake.segments[1:]:
       if snake.head.distance(seg) < 5:
            game_on = False
            score.game_over()

screen.exitonclick()

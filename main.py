from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the game screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates.

# Initialize the snake, food, and scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up key listeners for snake control.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen manually.
    time.sleep(0.1)  # Add a short delay to control the game speed.

    snake.move()  # Move the snake.

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new location.
        snake.extend()  # Extend the snake.
        scoreboard.increase_score()  # Increase the score.

    # Detect collision with the wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()  # Display the game over message.

    # Detect collision with the snake's tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass  # Skip checking collision with the snake's head.
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()  # Display the game over message.

# Allow the user to exit the game by clicking on the screen.
screen.exitonclick()

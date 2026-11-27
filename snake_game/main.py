import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen=Screen()
screen.setup(width=550, height=550)

# changing background color
screen.bgcolor("black")

# set title of screen
screen.title("My snake game")


screen.tracer(0)     #turns OFF animation

# TODO 1: CREATE THE SNAKE BODY
snake= Snake()

# TODO 3: CREATE THE SNAKE FOOD
food=Food()

# TODO 5: CREATE A SCOREBOARD
scoreboard=Scoreboard()

# TODO 2: MOVE THE SNAKE
game_is_on=True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")

while game_is_on:
    screen.update()  # updates the screen (used when animation is turned off)
    time.sleep(0.1)    #Pauses the entire program including screen for 0.1 seconds
    snake.move()

    # TODO 4: DETECT COLLISION WITH THE FOOD
    # Checks distance with food
    if snake.head.distance(food)<20:

        snake.increase_size()
        food.refresh()
        scoreboard.increase_score()

    # TODO 6: DETECT COLLISION WITH THE WALL
    if snake.head.xcor()>275 or snake.head.xcor()<-275 or snake.head.ycor()>275 or snake.head.ycor()<-275:
        # game_is_on=False
        # show GAME OVER message
        # scoreboard.show_game_over()
        scoreboard.reset_game()
        snake.remove_snake()
        snake.new_snake()



    # TODO 7: DETECT COLLISION WITH THE TAIL
    # for segment in snake.segments:
    #     if segment != snake.head:   # don't check first segment as it is head itself
    #         if snake.head.distance(segment)<10:
    #             game_is_on=False
    #             scoreboard.show_game_over()

    for segment in snake.segments[2:]:   # (start checking collision from second segment)
        if snake.head.distance(segment)<10:
            # game_is_on=False
            # scoreboard.show_game_over()
            scoreboard.reset_game()  # updates highscore and set score=0
            snake.new_snake()


screen.exitonclick()
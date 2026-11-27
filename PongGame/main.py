
import time

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_is_on=True

RIGHT_PADDLE_POSITION=(360,0)
LEFT_PADDLE_POSITION=(-360,0)

# TODO : CREATE THE SCREEN
screen= Screen()
screen.setup(800,550)
screen.bgcolor("black")
screen.title("PONG GAME")


# TODO : CREATE PADDLE
screen.tracer(0)
r_paddle=Paddle(RIGHT_PADDLE_POSITION)

# TODO : CREATE ANOTHER PADDLE
l_paddle=Paddle(LEFT_PADDLE_POSITION)

# TODO: CREATE THE BALL AND MAKE IT MOVE
ball=Ball()


#TODO:  MOVE THE PADDLE
screen.listen()
screen.onkey(r_paddle.move_up, "i")
screen.onkey(r_paddle.move_down, "k")
screen.onkey(l_paddle.move_up, "e")
screen.onkey(l_paddle.move_down, "d")


# TODO: KEEP SCORE
l_score=Scoreboard(-300,"Left Player")
r_score=Scoreboard(300,"Right Player")


def game_over():
    global game_is_on
    game_is_on=False

while game_is_on:
    time.sleep(ball.move_sleep)
    screen.update()
    ball.move()
    # TODO: DETECT COLLISION WITH THE WALL AND BOUNCE
    # horizontal wall collision
    # 270 ≈ half screen height (275) minus ball radius(tril and error exact would be=265)
    if ball.ycor()>=265 or ball.ycor()<=-260:
        ## print("wall collided")
        ball.bounce_y()

    # TODO: DETECT COLLISION WITH THE PADDLE

    # Paddle collision detection
    # Uses:
    # 1) x-position window to ensure collision only on paddle's front face
    # 2) distance check for vertical alignment
    # 3) x_move direction check to prevent double-bounce or rear collisions

    # CHECKS IT COLLIDES WITH RIGHT PADDLE
    if (
        350<=ball.xcor()<=370
        and ball.distance(r_paddle)<=60
        and ball.x_move>0  # ball is moving towards the right paddle
    ):
        ## print("ball collided")   #for debugging
        ball.bounce_x()

    # CHECKS IT COLLIDES WITH LEFT PADDLE
    elif(
            -370 <= ball.xcor() <= -350
            and ball.distance(l_paddle) <= 60
            and ball.x_move < 0    # ball is moving towards the left paddle
    ):
        ## print("ball collided")
        ball.bounce_x()


    # TODO: DETECT WHEN PADDLE MISSES
    # Detect paddle miss only after collision checks
    # Ensures missed balls are scored and game state updates correctly

    if ball.xcor()>=400:
        l_score.increase_score()
        if l_score.check_winner():
            game_over()
        ball.reset_ball()

    elif ball.xcor()<=-400:
        r_score.increase_score()
        if r_score.check_winner():
            game_over()
        ball.reset_ball()

screen.exitonclick()



from turtle import Turtle

SCREEN_LIMIT=275
PADDLE_HALF_HEIGHT=50   # AS FULL HEIGHT IS 4*20=80
MOVE_DISTANCE=20

# Inheriting Turtle Class
class Paddle(Turtle):

    def __init__(self,position):

        super().__init__()  # Can do everything that Turtle Class can do and have all attributed of Turtle class

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(90)
        self.speed("fastest")
        self.penup()
        self.goto(position)



    def move_up(self):

        # if self.ycor()<SCREEN_LIMIT-PADDLE_HALF_HEIGHT:
        #     self.forward(MOVE_DISTANCE)


        new_y = self.ycor() + MOVE_DISTANCE
        max_y = SCREEN_LIMIT - PADDLE_HALF_HEIGHT
        self.sety(min(new_y, max_y))


    def move_down(self):

        # if self.ycor()>-SCREEN_LIMIT+PADDLE_HALF_HEIGHT:
        #     self.backward(MOVE_DISTANCE)


        new_y = self.ycor() - MOVE_DISTANCE
        min_y = -SCREEN_LIMIT + PADDLE_HALF_HEIGHT
        self.sety(max(new_y, min_y))
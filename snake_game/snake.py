from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # 1, 2, 3 or 0, 1 ,2
MOVE_DISTANCE=20
UP= 90
DOWN=270
RIGHT=0
LEFT=180


# TODO 1: CREATE THE SNAKE BODY
class Snake:
    def __init__(self):
        # Create three square turtles (default 20px*20px roughly each) positioned on (0,0)(-20,0)(-40,0)
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    # def create_snake(self):
    #     for position in STARTING_POSITION:
    #         snake_segment = Turtle("square")
    #         snake_segment.penup()
    #         snake_segment.color("white")
    #
    #         snake_segment.setpos(position)
    #
    #         self.segments.append(snake_segment)
    #
    # def increase_size(self):
    #
    #     snake_new_segment=Turtle("square")
    #     snake_new_segment.penup()
    #     snake_new_segment.color("white")
    #
    #     # set new position as position of last segment of snake
    #     new_position=self.segments[-1].pos()
    #
    #     snake_new_segment.setpos(new_position)
    #     self.segments.append(snake_new_segment)


    ######################  SECOND METHOD######################################
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.setpos(position)
        self.segments.append(snake_segment)

    def increase_size(self):
        self.add_segment(self.segments[-1].pos())

    # TODO 2: MOVE THE SNAKE
    def move(self):

        """Move the snake forward by shifting each segment to the position of the one ahead.
        segment 2 move to position of segment 1 and segment 1 move to position of segment 0
        and segment 0 (aka snake head) move forward."""
        for seg_num in range(len(self.segments)-1, 0, -1):  # 2, 1, 0(excluded)
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)

        self.head.forward(MOVE_DISTANCE)

    def right(self):

        # doesn't allow snake to turn its head complete opposite(as it is not possible actually )
        if self.head.heading()!=LEFT:  # if its heading is left then can not set heading to right directly
            self.head.setheading(RIGHT)
            # self.move()



    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
            # self.move()



    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
            # self.move()

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
            # self.move()


    def new_snake(self):
        self.remove_snake()
        self.create_snake()
        self.head = self.segments[0]
        # self.move()

    def remove_snake(self):
        # segments ek Python list hai
        # clear() Python list ka built - in method hai

        for segment in self.segments:
            segment.goto(550,550)

        self.segments.clear()  # list empty ho jati hai





import random
from turtle import Turtle


# Inheriting Turtle class instead of making object of it
class Food(Turtle):

    # TODO 3: CREATE THE SNAKE FOOD
    def __init__(self):
        super().__init__()
        self.shape("circle")  # so it Can have everything of Turtle class
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # normally turtle is 20*20 but after stretching it to *0.5 it becomes 10 * 10

        self.color("orange")
        self.speed("fastest")
        self.refresh()



    #  Food goes to random position after Snake eats it
    def refresh(self):
        randx = random.randint(-255, 255)
        randy = random.randint(-255, 230)

        self.goto(randx, randy)
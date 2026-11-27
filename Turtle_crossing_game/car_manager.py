import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


from turtle import Turtle

class CarManager(Turtle):

    # Class Variable which is common for all objects unlike instance variable which is different for different objects
    
    

    STARTING_MOVE_DISTANCE = 5  # Class Variable: can be accessed using ClassName.class_variable
    MOVE_INCREMENT = 10
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1 ,stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=300,y=random.randint(-250,250))
        # self.move()



    def move(self):

        self.backward(CarManager.STARTING_MOVE_DISTANCE)

    @staticmethod
    def level_up():
        CarManager.STARTING_MOVE_DISTANCE+=CarManager.MOVE_INCREMENT









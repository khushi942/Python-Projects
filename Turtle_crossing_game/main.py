import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# CREATING PLAYER OBJECT
player=Player()

screen.listen()
screen.onkeypress(player.move,"Up")
scoreboard=Scoreboard()
game_is_on = True

game_loop=0
cars=[]

while game_is_on:


    time.sleep(0.1)
    screen.update()

    # After every 6th loop increase a car number(LEVEL 1-3)
    # After level 3 increase car number after every 3rd loop
    if scoreboard.level>3:
        if game_loop% 3==0:
            # Create Car Object
            car = CarManager()
            cars.append(car)


    else:
        if game_loop % 6==0:

            #Create Car Object
            car = CarManager()
            cars.append(car)


    game_loop += 1

    # Move each car in cars list
    for car in cars:
        car.move()
        # Game over when Player Collides with the Car
        if player.distance(car)<20:
            print("car collides")
            game_is_on=False
            scoreboard.game_over()


    # Resets the player to starting line when it reaches the FINISH LINE
    if player.ycor()>=player.finish_line:
        player.reset()
        scoreboard.update_level()
        CarManager.level_up()



screen.exitonclick()

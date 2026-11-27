#TODO 1: TYPE 'W' FOR 'FORWARDS'
# TODO 2: TYPE 'S' FOR 'BACKWARDS'
# TODO 3: TYPE 'A' FOR 'COUNTER- CLOCKWISE'
# TODO 4: TYPE 'D' FOR 'CLOCKWISE'
# TODO 5: TYPE 'C' FOR 'CLEAR DRAWING' AND PUT YOUR TURTLE BACK INTO CENTRE

from turtle import Turtle, Screen

tim=Turtle()
screen= Screen()

# tim.shape("turtle")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)




def clear_screen():
    # Clear the drawing
    tim.clear()
    # Move the turtle back to centre
    tim.teleport(0,0)



screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=move_counter_clockwise, key='a')
screen.onkey(fun=move_clockwise, key='d')


screen.onkey(fun=clear_screen, key='c')

screen.mainloop()

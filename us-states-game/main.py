import turtle
from turtledemo.penrose import star

import pandas
screen=turtle.Screen()
screen.title("U.S.States Game")
screen.setup(725,491)
# screen.bgpic("./blank_states_img.gif")

shape="./blank_states_img.gif"
screen.addshape(shape)
turtle.shape(shape)

# figure out the coordinates of each of the state in shape (image) relative to the entire screen(Already data is provided in csv file so need to manually do it)
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)  #event-driven programming. Whenever the user clicks on the screen, call this function
# turtle.mainloop()

data = pandas.read_csv("./50_states.csv")   # Data Frame
state_list = data.state.to_list()   # Series to list
game_is_on=True
score=0
guessed_states=[]

while len(guessed_states)<50:

    state_answer=screen.textinput(title=f"{score}/50 STATES CORRECT",
                                  prompt="What's another state's name?").title().strip()

    if state_answer=="Exit":

        # missing_states = []
        # for state in state_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        missing_states=[state for state in state_list if state not in guessed_states]

        s = pandas.Series(missing_states)
        s.to_csv("states_to_learn.csv", index=False)
        break

    if state_answer in state_list:

        guessed_states.append(state_answer)
        score+=1
        state_data= data[data.state==state_answer]   #series

        # state_row_x = state_data.x.to_list()[0]

        state_x_cor = state_data.x.item()   # gives the item value of x column
        state_y_cor = state_data.y.to_list()[0]  # 2nd way
        t=turtle.Turtle()
        t.hideturtle()
        t.teleport(state_x_cor, state_y_cor)
        t.write(state_answer)

        if len(guessed_states)==50:
            t = turtle.Turtle()
            t.hideturtle()
            t.teleport(-100,0)
            t.write("Well done", font=("Comic Sans MS", 46, "bold"))












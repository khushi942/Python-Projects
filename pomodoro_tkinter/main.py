

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
from tkinter import *
check_mark= ""
reps = 0   # repetitions
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps= 0


    # Stops the timer
    window.after_cancel(timer)

    # Resets the text in the timer
    canvas.itemconfig(timer_text,text = "00:00")

    # Resets the title
    title_label.configure(text="Timer", fg=GREEN)


    # Resets the checkmarks
    checkmarks_label.configure(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_mark

    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60




    # If it is 8th reps
    if reps % 8==0:
        count_down(long_break_sec)
        title_label.configure(text="Break", fg=RED)
        check_mark=""
        checkmarks_label.configure(text= check_mark)

    # If it is 2nd/4th/6th repetition
    elif reps % 2==0:
        title_label.configure(text="Break", fg=PINK)

        count_down(short_break_sec)

    # If it is 1st/3rd/5th/7th repetition
    else:
        title_label.configure(text="Work", fg=GREEN)
        count_down(work_sec)













# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time
# def timer():
#     count= 5
#     timer_label = Label(text=count)
#     timer_label.grid(row=1, column=1)
#     while count>=0:           ################## not a right approach as it is gui program and, it already has a mainloop ######
#         time.sleep(1)
#         timer_label.configure(text=count)
#         count -= 1
#         window.update()

# TODO: COUNTDOWN MECHANISM USING after() method

def count_down(count):
    global check_mark
    global timer
    count_min = count // 60   #floor division
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:

        count= count-1
        # calls the functions after 1000ms
        # Recursive calling the function reducing count by 1 each time
        timer= window.after(1000, count_down,count)    # 1000ms = 1 sec

        # the above line is asynchronous

    else:
        if reps % 2!=0:
            check_mark += "✔"
            checkmarks_label.configure(text=check_mark)

        start_timer()




# ---------------------------- UI SETUP ------------------------------- #



window= Tk()
window.title("Pomodoro")
window.configure(bg=YELLOW,
                 padx=100,pady=50)

tomato_img = PhotoImage(file="tomato.png")


# TODO: CREATE CANVAS FOR WRITING TIMER VALUE
# The highlightthickness option controls the width of this focus highlight border in pixels.
canvas = Canvas(window, width=200, height=224, highlightthickness=0)
canvas.configure(bg=YELLOW)

canvas.create_image(100, 112, image= tomato_img)  # put the image in center of canvas(102,112)


timer_text = canvas.create_text(100,130, text= "00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
# print(timer_text)  # 2 "It prints the ID of the create_text"


title_label=Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button= Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button= Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks_label= Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
checkmarks_label.grid(row=3, column=1)


window.mainloop()
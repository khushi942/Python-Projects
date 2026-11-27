import random
from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT =("Ariel", 40, "italic")
WORD_FONT = ("Comic Sans MS", 60, "bold")

current_card ={}

def flip_card():
    if not current_card:  # Safer
        return

    canvas.itemconfig(canvas_image,image=back_image)

    english_word = current_card["ENGLISH"]
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = english_word, fill = "white")

def next_card(choice):
    global current_card
    global flip_timer
    global to_learn

    # invalidate the previous timer when user click the button multiple times
    if flip_timer:
        window.after_cancel(flip_timer)

    canvas.itemconfig(canvas_image, image = front_image)

    if choice=="known" and current_card:
        if current_card in to_learn:   # safer
            to_learn.remove(current_card)
            updated_data = pd.DataFrame(to_learn)   # convert list of dict to dataframe
            updated_data.to_csv("./data/words_to_learn.csv", index=False)

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Done 🎉", fill="black")
        canvas.itemconfig(card_word, text="All learned!", fill= "black")
        return

    current_card = random.choice(to_learn)  # {"JAPANESE": "watashi", "ENGLISH": "I"},
    jap_word = current_card["JAPANESE"]
    canvas.itemconfig(card_title, text ="Japanese", fill = "black")
    canvas.itemconfig(card_word, text= jap_word, fill = "black")


    # After 3s(=3000ms) flip the card and show english translation
    flip_timer = window.after(3000,flip_card)    # .after don't take named arguments



def right_pressed():
    next_card("known")

def wrong_pressed():
    next_card("unknown")

window = Tk()
window.title("Flashy")
window.configure(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = None

# Note: Photoimage class should not be created inside a function otherwise it does not work
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file= "./images/card_back.png")



try:
    data = pd.read_csv("./data/words_to_learn.csv")

except (FileNotFoundError,  pd.errors.EmptyDataError):  # Also catch exception when there is file but no data to parse

    # opening japanese word csv
    data = pd.read_csv("./data/japanese_words.csv")


to_learn = data.to_dict(orient="records")  # orient ="records" give row wise list of dict--->
                                         # [
                                         #   {"JAPANESE": "watashi", "ENGLISH": "I"},
                                         #   {"JAPANESE": "anata", "ENGLISH": "you"}
                                         # ]




canvas = Canvas(window,
                width=800,
                height=526,
                highlightthickness=0,
                bg=BACKGROUND_COLOR
                )

canvas.grid(row=0, column=0, columnspan=2)
# in canvas position 0,0 means top left corner of the canvas
# Placing the image in center of canvas as 800/2=400 and 526/2=268
canvas_image = canvas.create_image(400,268,image=front_image)

card_title =  canvas.create_text(400, 150, text="", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)


right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=right_pressed)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button( image=wrong_image, highlightthickness=0, bd=0, command=wrong_pressed)
wrong_button.grid(row=1, column=1)

# Calling next_card to generate random card when program executes first time
next_card("unknown")

window.mainloop()

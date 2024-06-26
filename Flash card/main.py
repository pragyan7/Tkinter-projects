from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_MEANING = ("Arial", 60, "bold")

#----------------------CREATE NEW FLASH CARDS----------------------#
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=white_card)
    flip_timer = window.after(3000, func=flip_card)

#----------------------FLIP THE CARD----------------------#
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=green_card)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#----------------------CARD IS KNOWN----------------------#
def is_known():
    to_learn.remove(current_card)
    
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#----------------------CREATE UI----------------------#
canvas = Canvas(width=800, height=526)
white_card = PhotoImage(file="images/card_front.png")
green_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=white_card)

card_title = canvas.create_text(400, 150, text="", font=FONT_LANGUAGE)
card_word = canvas.create_text(400, 263, text="", font=FONT_MEANING)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

next_card()


window.mainloop()

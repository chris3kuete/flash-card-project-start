from tkinter import *
import random
import pandas
import csv

BACKGROUND_COLOR = "#B1DDC6"
initial_card = {}
frenchDict = {}


def next_click_cross():
    global initial_card
    global switch_timer

    window.after_cancel(switch_timer)  # to cancel the timer everytime we go to a new card
    initial_card = random.choice(frenchDict)
    canvas.itemconfig(initialImage, image=cardFrontImage)
    canvas.itemconfig(title_id, text="French", fill='black')
    canvas.itemconfig(words_id, text=initial_card['French'], fill='black')
    switch_timer = window.after(3000, turn_card)


def already_know():
    frenchDict.remove(initial_card)
    data1 = pandas.DataFrame(frenchDict)
    data1.to_csv("data/words_not_known.csv", index=False)
    print(len(frenchDict))
    next_click_cross()


def turn_card():
    canvas.itemconfig(turn_image, image=cardBackImage)
    canvas.itemconfig(title_id, text="English", fill='white')
    canvas.itemconfig(words_id, text=initial_card["English"], fill='white')


window = Tk()
window.title("Learn English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

switch_timer = window.after(3000, turn_card)

canvas = Canvas(width=800, height=526)
cardFrontImage = PhotoImage(file="images/card_front.png")
initialImage = canvas.create_image(400, 263, image=cardFrontImage)
title_id = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
words_id = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=800, height=526)
cardBackImage = PhotoImage(file="images/card_back.png")
turn_image = canvas.create_image(400, 263, image=cardBackImage)
title_id1 = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
words_id1 = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_click_cross, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=already_know, highlightthickness=0)
right_button.grid(row=1, column=1)

try:
    data = pandas.read_csv("data/words_not_known.csv")
except FileNotFoundError:
    source_file = pandas.read_csv("data/french_words.csv")
    frenchDict = source_file.to_dict(orient="records")
else:
    frenchDict = data.to_dict(orient="records")

next_click_cross()

window.mainloop()

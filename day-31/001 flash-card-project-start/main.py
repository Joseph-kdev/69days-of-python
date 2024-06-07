from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    values = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = values.to_dict(orient="records")
    
    
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill= "black")
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)

def is_known():
    to_learn.remove(current_card)
    
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width= 800, height= 526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image= card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_back_img = PhotoImage(file="./images/card_back.png")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


canvas.config(background= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0, column=0, columnspan= 2)


correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image= correct_img, highlightthickness= 0, command= is_known)
correct_button.grid(row= 1, column= 1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image= wrong_img, highlightthickness= 0, command= next_card)
wrong_button.grid(row= 1, column=0)

next_card()

window.mainloop()


from tkinter import *
from turtle import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data=pandas.read_csv("data/words_left_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")



def is_known():
    to_learn.remove(current_card)
    next_card()
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_left_to_learn.csv",index=False)

def next_card():
    global current_card
    global fliptimer
    window.after_cancel(fliptimer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    fliptimer=window.after(3000,func=flip_Card)

def flip_Card():
    canvas.itemconfig(card_title,text="English",fill="WHite")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
fliptimer=window.after(3000,func=flip_Card)
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="images/right.png")
known_button=Button(image=check_image,command=is_known,highlightthickness=0)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()

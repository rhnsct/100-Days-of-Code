from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
to_learn = {}



try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")

def new_card():  
    global random_card, flip_after
    window.after_cancel(flip_after)
    try:
        random_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo("Empty", "No more things to learn.")
        
    french_word = random_card["French"].capitalize()
    canvas.itemconfig(canvas_background, image=card_front)
    canvas.itemconfig(text_language, text=french_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_after = window.after(3000, flip_card)
    
    


def flip_card():
    global random_card
    english_word = random_card["English"].capitalize()
    canvas.itemconfig(canvas_background, image=card_back)
    canvas.itemconfig(text_language, text=english_word, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

  
def learned_word():
    to_learn.remove(random_card)
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    new_card()
    
    

#---------------------------------- UI -----------------------------------------#
window = Tk()
window.title("Flashcard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_after = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
text_language = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, bd=0, highlightthickness=0, command=learned_word)
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, bd=0, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)





new_card()

window.mainloop()

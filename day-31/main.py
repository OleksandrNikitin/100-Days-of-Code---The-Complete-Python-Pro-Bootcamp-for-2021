import secrets
from tkinter import PhotoImage, Button, Tk, Canvas

import pandas
from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN = "data/words_to_learn.csv"
ORIGINAL_WORDS = "data/french_words.csv"
current_card = {}

try:
    with open(WORDS_TO_LEARN, "r") as words_to_learn_file:
        data = pandas.read_csv(words_to_learn_file)
except FileNotFoundError:
    with open(ORIGINAL_WORDS, "r") as french_words_file:
        data = pandas.read_csv(french_words_file)
except pandas.errors.EmptyDataError:
    with open(ORIGINAL_WORDS, "r") as french_words_file:
        data = pandas.read_csv(french_words_file)
finally:
    to_learn = DataFrame.to_dict(data, orient="records")


def next_card():
    global current_card, flip_timer, to_learn
    window.after_cancel(flip_timer)
    language = "French"

    current_card = secrets.choice(to_learn)
    current_word = current_card[language]
    canvas.itemconfig(canvas_background, image=front_image)
    canvas.itemconfig(card_title, text=language, fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    language = "English"

    current_word = current_card[language]
    canvas.itemconfig(canvas_background, image=back_image)
    canvas.itemconfig(card_title, text=language, fill="white")
    canvas.itemconfig(card_word, text=current_word, fill="white")


def save_words_to_learn():
    global current_card, to_learn
    to_learn.remove(current_card)
    df_to_save = pandas.DataFrame(to_learn)
    df_to_save.to_csv(WORDS_TO_LEARN, index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=front_image)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 30, "bold"))

canvas.grid(column=0, row=0, columnspan=2)
right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image, highlightthickness=0, command=save_words_to_learn
)

right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)

wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

from tkinter import *
from btn import Btn
import pandas
import random
# ------------------------------ CONSTANTS & VARIABLES -------------------------------- #
BG_COLOR = "#B1DDC6"
CARD_BACK_COLOR = '#91C2AF'
words_known = []
LANG_FONT = ('Open Sans', 30)
FONT = ('Open Sans', 50, 'bold')

# ---------------------------------- WORD HANDLING ------------------------------------ #

french_csv = pandas.read_csv('./data/french_words.csv')
french = french_csv.French
english = french_csv.English
random_french_word = random.choice(french)


# ----------------------------------- FLIP CARD --------------------------------------- #
def flip_card(english_translation):
    Label.config(card_front, image=imgCardBack)
    Label.config(language_name, text="English", bg=CARD_BACK_COLOR)
    Label.config(french_label, text=str(english_translation), bg=CARD_BACK_COLOR)


# ----------------------------------- GET NEW WORD ------------------------------------- #
def get_new_word():
    global random_french_word
    random_french_word = random.choice(french)
    for word in words_known:
        if random_french_word == word:
            get_new_word()
    Label.config(card_front, image=imgCardFront)
    Label.config(language_name, text='French', bg='#ffffff')
    Label.config(french_label, text=random_french_word, bg='#ffffff')
    english_word = french_csv[french == random_french_word].English.to_string(index=False)
    root.after(5000, flip_card, english_word)


# -------------------------------- REMOVE KNOWN WORDS ---------------------------------- #
def remove_known():
    words_known.append(random_french_word)
    get_new_word()


# ---------------------------------------- UI ------------------------------------------ #

# MAIN WINDOW
root = Tk()
root.configure(bg=BG_COLOR, highlightthickness=0, padx=50, pady=10)
root.title('French Flash Cards')
root.iconbitmap('./images/index.ico')
root.minsize(width=900, height=650)

# IMAGES
imgCardFront = PhotoImage(file='./images/card_front.png')
imgCardBack = PhotoImage(file='./images/card_back.png')
imgRight = PhotoImage(file='./images/right.png')
imgRightHover = PhotoImage(file='./images/right-darker.png')
imgWrong = PhotoImage(file='./images/wrong.png')
imgWrongHover = PhotoImage(file='./images/wrong-darker.png')

# LABELS
card_front = Label(root, image=imgCardFront, bg=BG_COLOR)
card_front.place(rely=0, relx=.5, anchor='n')

language_name = Label(root, font=LANG_FONT, background='#ffffff', text='French')
language_name.pack(pady=80)

french_label = Label(root, font=FONT, background='#ffffff')
french_label.pack()

# BUTTONS
right_button = Btn(root, imgRight, imgRightHover, bg=BG_COLOR, borderwidth=0,
                   activebackground=BG_COLOR, command=remove_known)
right_button.pack(side='right', anchor='se')

wrong_button = Btn(root, imgWrong, imgWrongHover, bg=BG_COLOR, borderwidth=0,
                   activebackground=BG_COLOR, command=get_new_word)
wrong_button.pack(side='left', anchor='sw')

get_new_word()
root.mainloop()

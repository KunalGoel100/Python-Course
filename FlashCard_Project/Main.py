from pickle import GLOBAL
from tkinter import *
import pandas
import random

count = 0
idx = 0
rem = 0
screen = Tk()
screen.config(bg="#B1DDC6",padx=50,pady=50)
canvas = Canvas(height=526,width=800,bg="#B1DDC6",highlightthickness=0)
canvas.grid(row=1,column=1,columnspan=2)

Green = PhotoImage(file="images/card_back.png")
White = PhotoImage(file="images/card_front.png")
Tile = canvas.create_image(400,263,image=Green)

Cross = PhotoImage(file="images/nope.png")
CrossButton = Button(image=Cross,highlightthickness=0,borderwidth=0)
CrossButton.grid(row=2,column=1)

Tick = PhotoImage(file="images/yes.png")
TickButton = Button(image=Tick, highlightthickness=0, borderwidth=0)
TickButton.grid(row=2, column=2)

Language = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
Word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

file = pandas.read_csv("french_words2.csv")
data = file.to_dict()



def RandomWord():
    global count, rem, idx
    if len(data["French"]) == 0:
        canvas.itemconfig(Language, text="Completed")
        canvas.itemconfig(Word, text="")

    elif count == 0:
        idx = random.randint(0, 100)
        canvas.itemconfig(Tile, image=Green)
        canvas.itemconfig(Language,text="French")
        try:
            canvas.itemconfig(Word,text=data["French"][idx])
        except:
            RandomWord()
        else:
            count += 1
    elif count == 1:
        Flip()
        count = 0


def Flip():
    global idx
    canvas.itemconfig(Tile,image=White)
    canvas.itemconfig(Language,text="English")
    canvas.itemconfig(Word,text=data["English"][idx])

def Remove():
    global idx
    data["French"].pop(idx)
    data["English"].pop(idx)
    print(idx)
    print(data)

def TickAction():
    global count, rem
    if count == 0:
        rem = 1
    if rem == 1:
        Remove()
        rem = 0
    RandomWord()



TickButton.config(command=TickAction)
CrossButton.config(command=RandomWord)
RandomWord()
screen.mainloop()
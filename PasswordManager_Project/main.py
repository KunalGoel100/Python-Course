from tkinter import *
import random
import pyperclip
import pandas
from pandas import *
screen = Tk()
screen.minsize(height=500, width=520)
screen.config(padx=100,bg="white")

canvas = Canvas(height=400,width=300,bg="white",highlightthickness=0)
logoImage = PhotoImage(file="PadLock_Image.png")
canvas.create_image(150,200,image=logoImage)
canvas.place(x=0,y=0)

##################################
text_Website = Label(text="Website", width=14, bg="white", font=("ariel",10,"bold"))
text_Website.place(x=-85,y=400)
#
text_Email = Label(text="Email/Username", width=14, bg="white", font=("ariel",10,"bold"))
text_Email.place(x=-85,y=430)
#
text_Password = Label(text="Password", width=14, bg="white", font=("ariel",10,"bold"))
text_Password.place(x=-85,y=460)
# ##################################
entry_website = Entry(width=34,borderwidth=2)
entry_website.place(x=30,y=400)
#
entry_Email = Entry(width=34,borderwidth=2)
entry_Email.place(x=30,y=430)
entry_Email.insert(0, string="kunal.goel@zf.com")
#
entry_Password = Entry(width=34,borderwidth=2)
entry_Password.place(x=30,y=460)
# #################################
def GeneratePassword():
    number = [1,2,3,4,5,6,7,8,9]
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    symbol = ["!","@","#","$","%","^","&","*","(",")","_","+"]
    characters = [number,alphabet,symbol]
    password = []
    NewPassword = []
    FinalPassword = ""
    for i in range(0,random.randint(8,20),1):
        x = random.randint(0,2)
        password.append(random.sample(characters[x],1))
    for j in password:
        NewPassword.append(j[0])
    for j in NewPassword:
        FinalPassword += str(j)
    entry_Password.delete(0,END)
    entry_Password.insert(0,string=FinalPassword)
    pyperclip.copy(FinalPassword)

button_Generate = Button(text="Generate Password",border=0.5, command=GeneratePassword, width=16)
button_Generate.place(x=280,y=425)
#
def CheckRepetition():
    count = CheckEmpty()
    if count == 0:
        file = pandas.read_csv("Password_Storage.csv")
        if entry_website.get() in file.Website.values:
            print("Duplicate")
            canvas.itemconfig(error_message, text="Duplicate Website", fill="#ff7f50")
        else:
            canvas.itemconfig(error_message, text="Added to Storage", fill="#008000")
            AddToStorage()
    elif count == 1:
        print("Enter Website")
        canvas.itemconfig(error_message,text="Enter Website", fill="#cf1020")
    elif count == 2:
        print("Enter Email/Username")
        canvas.itemconfig(error_message, text="Enter Email/Username", fill="#cf1020")
    elif count == 3:
        print("Enter Password")
        canvas.itemconfig(error_message, text="Enter Password", fill="#cf1020")

def CheckEmpty():
    count = 0
    if entry_website.get() == "":
        count = 1
    elif entry_Email.get() == "":
        count = 2
    elif entry_Password.get() == "":
        count = 3
    return count

def AddToStorage():
    file = open("Password_Storage.csv","a")
    file.write(f"{entry_website.get()},{entry_Email.get()},{entry_Password.get()}\n")
    file.close()
    entry_Password.delete(0,END)
    entry_website.delete(0,END)

button_Add = Button(text="Add to storage",border=0.5, command=CheckRepetition, width=16)
button_Add.place(x=280,y=455)
#
def Search():
    file = pandas.read_csv("Password_Storage.csv")
    temp = file[file.Website == entry_website.get()]
    print(temp.Password)
    if not temp.empty:
        entry_Password.delete(0, END)
        entry_Password.insert(0, string=temp.Password.values[0])
        entry_Email.delete(0,END)
        entry_Email.insert(0,string=temp.Username.values[0])

button_Search = Button(text="Search",border=0.5, command=Search, width=16)
button_Search.place(x=280,y=395)
#
error_message = canvas.create_text(150,220,text="",font=("Ariel",15,"bold"),fill="black")



















screen.mainloop()

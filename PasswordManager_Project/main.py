from tkinter import *

screen = Tk()
screen.minsize(height=500, width=500)
screen.config(padx=100,bg="white")

canvas = Canvas(height=400,width=300,bg="white",highlightthickness=0)
logoImage = PhotoImage(file="PadLock_Image.png")
canvas.create_image(150,200,image=logoImage,)
canvas.place(x=0,y=0)

##################################
text_Website = Label(text="Website")
text_Website.place(x=-80,y=400)
#
text_Email = Label(text="Email/Username")
text_Email.place(x=-80,y=430)
#
text_Password = Label(text="Password")
text_Password.place(x=-80,y=460)
# ##################################
entry_website = Entry(width=34,borderwidth=2)
entry_website.place(x=30,y=400)
#
entry_Email = Entry(width=34,borderwidth=2)
entry_Email.place(x=30,y=430)
#
entry_Password = Entry(width=34,borderwidth=2)
entry_Password.place(x=30,y=460)
# #################################
button_Generate = Button(text="Generate Password")
button_Generate.place(x=200,y=430)
#
# button_Add = Button(text="Add to storage")
# button_Add.place()
#














screen.mainloop()

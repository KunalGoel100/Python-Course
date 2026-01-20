from tkinter import *

screen = Tk()





def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100,command=scale_used)
scale.pack()

screen.mainloop()
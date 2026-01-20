from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLACK = "#000000"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- TIMER RESET ------------------------------- # 
count=0
BCount = 0
countdown = None
Work = 0.1
Break = 0.1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def call_Timer():
    Timer(int(Work * 60))
    disp_Work()
def call_Break():
    Timer(int(Break * 60))
def reset_timer():
    screen.after_cancel(countdown)
    canvas.itemconfig(Timer_text, text=f"00:00")
    global count
    global BCount
    count = 0
    BCount = 0
    disp_blank()
    disp_Timer()
def WorkTime(value):
    global Work
    Work = int(value)
def BreakTime(value):
    global Break
    Break = int(value)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def Timer(tim):
    # disp_Work()
    count_min = int(tim / 60)
    count_sec = tim % 60
    format = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if count_sec < 10 and count_sec >= 0:
        count_sec = format[count_sec]
    if count_min < 10 and count_min >= 0:
        count_min = format[count_min]
    global count
    global BCount
    print(f"count={count}")
    print(f"BCount={BCount}")
    canvas.itemconfig(Timer_text, text=f"{count_min}:{count_sec}")
    if tim>0:
        global countdown
        countdown = screen.after(1000, Timer, tim-1)
    elif tim<=0:

        if count < 4 and BCount == 0:
            Tick(count)
            call_Break()
            disp_Break()
            BCount = 1
        elif count < 4:
            disp_Timer()
            BCount = 0
            print(count)
            count += 1
            call_Timer()
        else:
            Tick(count)
            canvas.itemconfig(Timer_text, text=f"OVER")
            print("Over")

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")
screen.config(bg="#f7f5dd")
screen.minsize(width=400,height=350)

# screen.after(1000,Timer,10)
def Tick(count):
    for i in range(0,count+1,1):
        tick = Label(text="✔️", bg=YELLOW)
        tick.place(x=150+i*20,y=300)

def disp_blank():
    blank = Button(text="",padx=50,bg=YELLOW,border=0)
    blank.place(x=150,y=300)
def disp_Break():
    text.config(text="Break",fg=PINK)
def disp_Timer():
    text.config(text="Timer",fg=BLACK)
def disp_Work():
    text.config(text="Work",fg=RED)

text = Label(text="Timer",font=("Courier",30,"bold"),bg="#f7f5dd",fg=BLACK)
# text.config(fg=GREEN)
text.grid(row=1, column=2)
startButton = Button(text="Start",padx=10, bg=GREEN, border=1)
startButton.place(x=80,y=300)
startButton.config(command=call_Timer)
resetButton = Button(text="Reset",padx=10, bg=GREEN, border=1)
resetButton.place(x=270,y=300)
resetButton.config(command=reset_timer)

canvas = Canvas(width=400, height=245)
canvas.config(bg="#f7f5dd", highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(200,120,image=tomato)
Timer_text=canvas.create_text(200,140,text="00:00",font=("Courier",30,"bold"))
canvas.grid(row=2, column=2)

WorkTimeSlider = Scale(from_=0, to=100, resolution=5, bg=YELLOW, highlightthickness=0, command= WorkTime)
WorkTimeSlider.place(x=310,y=140)
WorkTimeText = Label(text="Work",bg= YELLOW, fg=PINK, font=("Courier",15,"bold"))
WorkTimeText.place(x=315,y=240)

BreakTimeSlider = Scale(from_=0, to=100, resolution=5, bg=YELLOW, highlightthickness=0, command= BreakTime)
BreakTimeSlider.place(x=30,y=140)
BreakTimeText = Label(text="Break",bg= YELLOW, fg=PINK, font=("Courier",15,"bold"))
BreakTimeText.place(x=30,y=240)

screen.mainloop()
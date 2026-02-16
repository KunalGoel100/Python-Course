from tkinter import *
from question_model import Question

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self,quiz):
        self.Quiz = quiz
        self.window = Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,bg="#fdfff5")
        self.canvas.grid(row=2,column=1,columnspan=2,pady=20)

        tick = PhotoImage(file="images/true.png")
        cross = PhotoImage(file="images/false.png")

        self.Tick_Button = Button(image=tick,borderwidth=0,command=self.Yes_Button)
        self.Tick_Button.grid(row=3,column=1,pady=20,)

        self.Cross_Button = Button(image=cross,borderwidth=0,command=self.No_Button)
        self.Cross_Button.grid(row=3,column=2,pady=20)

        self.Score = Label(text=f"Score: {self.Quiz.score}",font=("Ariel",12,"bold"),fg="white",bg=THEME_COLOR)
        self.Score.grid(row=1,column=2)

        self.question = self.canvas.create_text(150,125,text="Question",font=("Ariel",20,"italic"),fill=THEME_COLOR,width=280)
        self.NextQuestion()
        self.window.mainloop()

    def NextQuestion(self):
        Ans = self.Quiz.still_has_questions()
        if Ans:
            q_next = self.Quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_next)
        else:
            self.canvas.itemconfig(self.question,text=f"Final Score: {self.Quiz.score}/{self.Quiz.question_number}")
            self.Tick_Button.config(state="disabled")
            self.Cross_Button.config(state="disabled")
    def Yes_Button(self):
        Ans = self.Quiz.check_answer("True")
        self.Feedback(Ans)

    def No_Button(self):
        Ans = self.Quiz.check_answer("False")
        self.Feedback(Ans)

    def Feedback(self,Ans):
        if Ans == True:
            self.canvas.config(bg="green")
            self.window.after(1000,self.Feedback,2)
        elif Ans == False:
            self.canvas.config(bg="red")
            self.window.after(1000,self.Feedback,2)
        else:
            self.canvas.config(bg="#fdfff5")
            self.Score.config(text=f"Score: {self.Quiz.score}")
            self.NextQuestion()
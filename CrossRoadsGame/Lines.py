import turtle as T

class line:
    def __init__(self,start):
        S = start
        temp = T.Turtle()
        temp.penup()
        temp.pensize(5)
        temp.goto(S[0],S[1])
        temp.setheading(0)
        temp.color('black')
        self.Tim = temp
        for i in range(0,27,1):
            self.Tim.forward(12)
            self.Tim.pendown()
            self.Tim.forward(12)
            self.Tim.penup()
        self.Tim.hideturtle()






import turtle as T

class line:
    def __init__(self):
        self.Line = T.Turtle()
        self.Line.penup()
        self.Line.pensize(5)
        self.Line.color('white')
        self.Line.goto(0,380)
        self.Line.right(90)
        for i in range(0,38,1):
            self.Line.pendown()
            self.Line.forward(10)
            self.Line.penup()
            self.Line.forward(10)
        self.Line.hideturtle()
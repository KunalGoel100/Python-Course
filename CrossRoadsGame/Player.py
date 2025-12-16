import turtle as T

class player:
    def __init__(self):
        temp = T.Turtle()
        temp.shape('turtle')
        temp.color('white')
        temp.penup()
        temp.goto(0,-230)
        temp.setheading(90)
        temp.shapesize(1)
        self.Player = temp

    def Left(self):
        pos = self.Player.pos()
        if pos[0] >= -300:
            self.Player.goto(pos[0] - 5, pos[1])
    def Right(self):
        pos = self.Player.pos()
        if pos[0] <= 300:
            self.Player.goto(pos[0] + 5, pos[1])
    def Up(self):
        pos = self.Player.pos()
        if pos[1] <= 200:
            self.Player.goto(pos[0], pos[1] + 5)


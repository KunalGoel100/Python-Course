import turtle as T

class Player:
    def __init__(self):
        self.Box = []
        for i in range(0,3,1):
            temp = T.Turtle()
            temp.penup()
            temp.speed(10)
            temp.color('white')
            temp.shape('square')
            temp.goto(0,-220)
            temp.forward(-i*20)
            self.Box.append(temp)
    def Left(self):
        if self.Box[len(self.Box)-1].xcor() > -230:
            for i in range(0, 3, 1):
                self.Box[i].forward(-40)

    def Right(self):
        if self.Box[0].xcor() < 220:
            for i in range(0, 3, 1):
                self.Box[i].forward(40)




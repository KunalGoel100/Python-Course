import turtle as T

class score:
    def __init__(self,type):
        if type == 1:
            self.PScore = 0
            temp = T.Turtle()
            temp.penup()
            temp.goto(0,240)
            temp.write("0",False,"center",["Arial",60,"normal"])
            temp.hideturtle()
            self.ScoreDisplay = temp
        elif type == 2:
            temp = T.Turtle()
            temp.penup()
            temp.hideturtle()
            self.OutDisplay = temp

    def UpdateScore(self):
        self.PScore += 1
        self.ScoreDisplay.clear()
        self.ScoreDisplay.write(self.PScore,False,"center",["Arial",60,"normal"])
        return self.PScore

    def Out(self):

        self.OutDisplay.write("Game Over",False,"center",["Arial",80,"normal"])
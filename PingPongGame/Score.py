import turtle as T

class score:
    def __init__(self):
        self.Score = []
        self.SS = [0,0]
        for i in range(0,2,1):
            Tim = T.Turtle()
            Tim.goto((-1+(i*2))*50,280)
            Tim.color('white')
            Tim.hideturtle()
            Tim.write(self.SS[i],False,'center',('Ariel',80,'normal'))
            self.Score.append(Tim)

    def SUpdate(self,id):
        self.SS[id] += 1
        self.Score[id].clear()
        self.Score[id].write(self.SS[id],False,'center',('Ariel',80,'normal'))

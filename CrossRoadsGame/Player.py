import turtle as T
import Score
class player:
    def __init__(self):
        temp = T.Turtle()
        temp.shape('circle')
        temp.color('black')
        temp.penup()
        temp.goto(0,-230)
        temp.setheading(90)
        temp.shapesize(1)
        self.Player = temp
        self.score = Score.score(1)
        self.Score = 1

    def Left(self):
        pos = self.Player.pos()
        if pos[0] >= -300:
            self.Player.goto(pos[0] - 10, pos[1])
    def Right(self):
        pos = self.Player.pos()
        if pos[0] <= 300:
            self.Player.goto(pos[0] + 10, pos[1])
    def Up(self):
        pos = self.Player.pos()
        self.Player.goto(pos[0], pos[1] + 7)
    def Next(self):

        if self.Player.ycor() >= 190:
            self.Player.goto(0,-230)
            self.Score += self.score.UpdateScore()
            return [self.Score,10]
        return [self.Score,0]



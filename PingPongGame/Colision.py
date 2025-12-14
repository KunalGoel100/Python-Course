import Ball
import random
import Score
class colision:
    def __init__(self,ball,player):
        self.ball = ball
        self.player = player
        self.PScore = 0
        self.CScore = 0
        self.score = Score.score()

    def colide(self):
        for i in range(0,4,1):
            if self.player.Player[i].distance(self.ball.Ball) <= 10:
                self.ball.Strike()

    def out(self):
        if self.ball.Ball.xcor() < -400:
            print('Player Out')
            self.CScore += 1
            print(self.CScore)
            self.ball.Ball.goto(0,0)
            self.ball.Ball.setheading(random.randint(0, 360))
            self.score.SUpdate(1)

        elif self.ball.Ball.xcor() > 400:
            print("Computer Out")
            self.PScore += 1
            print(self.PScore)
            self.ball.Ball.goto(0, 0)
            self.ball.Ball.setheading(random.randint(0,360))
            self.score.SUpdate(0)


import turtle as T
import random

class player:
    def __init__(self):
        self.Player = []
        self.gameon = 1
        for i in range(0,4,1):
            temp = T.Turtle()
            temp.penup()
            temp.shape('square')
            temp.color('white')
            temp.goto(-380,i*20)
            temp.left(90)
            self.Player.append(temp)
    def Up(self):
        if self.Player[2].ycor() <= 380:
            for i in range(0,4,1):
                self.Player[i].forward(30)
    def Down(self):
        if self.Player[0].ycor() >= -380:
            for i in range(0,4,1):
                self.Player[i].forward(-30)
    def Stop(self):
        self.gameon = 0

class ball:
    def __init__(self):
        self.Ball = T.Turtle()
        self.Ball.shape('circle')
        self.Ball.color('white')
        self.Ball.penup()
        self.Ball.speed(1)
        self.Ball.setheading(random.randint(0,360))

    def move(self):
        self.Ball.forward(0.3)



    def Wall(self):
        if self.Ball.ycor() >= 380 or self.Ball.ycor() <= -380:
            angle = self.Ball.heading()
            self.Ball.setheading(360-angle)


    def Strike(self):
        angle = self.Ball.heading()
        if angle <= 180:
            self.Ball.setheading(180 - angle)
        else:
            self.Ball.setheading(540 - angle)

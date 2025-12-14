import turtle as T
import random as R
class Computer:
    def __init__(self,ball):
        self.ball = ball
        self.Comp = []
        for i in range(0,4,1):
            comp = T.Turtle()
            comp.shape('square')
            comp.setheading(90)
            comp.color('white')
            comp.penup()
            comp.speed(10)
            comp.goto(380,i*20)
            self.Comp.append(comp)

    def follow(self):
        x = self.ball.Ball.xcor()
        y = self.ball.Ball.ycor()
        for i in range(0, 4, 1):
            self.Comp[i].goto(380,y+(i*20))


    def Up(self):
        if self.Comp[2].ycor() <= 380:
            for i in range(0,4,1):
                self.Comp[i].forward(30)

    def Down(self):
        if self.Comp[0].ycor() >= -380:
            for i in range(0,4,1):
                self.Comp[i].forward(-30)


    def CompColide(self):
        for i in range(0,4,1):
            if self.Comp[i].distance(self.ball.Ball) <= 10:
                self.ball.Strike()

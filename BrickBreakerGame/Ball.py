import turtle as T
import random as R
import time

class Ball:
    def __init__(self):
        b = T.Turtle()
        b.penup()
        b.shape("circle")
        b.speed('fastest')
        b.shapesize(1,1)
        b.color('white')
        b.setheading(R.randint(0, 360))

        self.ball = b
        self.angle = 0

    def RightWall(self):
        self.angle = self.ball.heading()
        if self.angle <= 90:
            newAngle = 180 - self.angle
            self.ball.setheading(newAngle)
        else:
            newAngle = 540 - self.angle
            self.ball.setheading(newAngle)

    def LeftWall(self):
        self.angle = self.ball.heading()
        if self.angle <= 180:
            newAngle = 180 - self.angle
            self.ball.setheading(newAngle)
        else:
            newAngle = 540 - self.angle
            self.ball.setheading(newAngle)

    def TopWall(self):
        self.angle = self.ball.heading()
        newAngle = 360 - self.angle
        self.ball.setheading(newAngle)

    def BottomWall(self):
        self.angle = self.ball.heading()
        newAngle = 360 - self.angle
        self.ball.setheading(newAngle)

    def Check(self):
        if self.ball.xcor() >= 240:
            self.RightWall()
            return 1
        if self.ball.xcor() <= -240:
            self.LeftWall()
            return 1
        if self.ball.ycor() >= 240:
            self.TopWall()
            return 1
        if self.ball.ycor() <= -250:
            print("over")
            return 0
        else:
            return 1

    def Move(self):
        self.ball.forward(3)

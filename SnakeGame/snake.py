import turtle as T
import time
import random

class Snake:
    def __init__(self):
        f = T.Turtle()
        f.color('red')
        f.shape('square')
        f.shapesize(0.4,0.4)
        f.penup()

        Sc = T.Turtle()
        Sc.penup()
        Sc.hideturtle()
        Sc.color("white")
        Sc.setposition(0, 210)
        self.ScoreT = Sc

        self.food = f
        self.SnakeBody = []
        self.score = 0
        for i in range(0,3,1):
            Box = T.Turtle()
            Box.color('white')
            Box.shape('square')
            Box.shapesize(0.8, 0.8)
            Box.penup()
            Box.forward(-i*20)
            self.SnakeBody.append(Box)


    def Move(self):
        Screen = T.Screen()
        Screen.tracer(0)
        for i in range(len(self.SnakeBody) - 1, 0, -1):
            self.SnakeBody[i].goto(self.SnakeBody[i - 1].pos())
            # time.sleep(0.5/len(self.SnakeBody))
            # Screen.tracer(1)
            # Screen.update()
            # Screen.tracer(0)


        self.SnakeBody[0].forward(20)
        Screen.update()

    def up(self):
        if self.SnakeBody[0].heading() != 270:
            self.SnakeBody[0].setheading(90)
    def down(self):
        if self.SnakeBody[0].heading() != 90:
            self.SnakeBody[0].setheading(270)
    def left(self):
        if self.SnakeBody[0].heading() != 0:
            self.SnakeBody[0].setheading(180)
    def right(self):
        if self.SnakeBody[0].heading() != 180:
            self.SnakeBody[0].setheading(0)

    def Boundarycheck(self):
        if self.SnakeBody[0].xcor() < -250 or self.SnakeBody[0].xcor() > 250:
            print('Wall Collision')
            self.ScoreT.goto(0,0)
            self.ScoreT.write("GAME OVER", False, "center", ("Arial", 15, "normal"))
            return 0
        if self.SnakeBody[0].ycor() < -250 or self.SnakeBody[0].ycor() > 250:
            print('Wall Collision')
            self.ScoreT.goto(0, 0)
            self.ScoreT.write("GAME OVER", False, "center", ("Arial", 15, "normal"))
            return 0
        else:
            return 1
    def Selfcheck(self):
        for i in range(1,len(self.SnakeBody),1):

            if self.SnakeBody[0].distance(self.SnakeBody[i]) < 10:
                print('Self Collision')
                self.ScoreT.goto(0, 0)
                self.ScoreT.write("GAME OVER", False, "center", ("Arial", 15, "normal"))

                return 0
        return 1
    def randomfood(self):
        Screen = T.Screen()
        posx = random.randint(-11,11)*20
        posy = random.randint(-11,11)*20
        Screen.tracer(0)
        self.food.setposition((posx,posy))
        Screen.tracer(0)
    def checkFood(self):
        if self.SnakeBody[0].distance(self.food) < 10:
            self.randomfood()
            self.increaseSize()
            self.Score()
    def increaseSize(self):
        Box = T.Turtle()
        Box.color('white')
        Box.shape('square')
        Box.shapesize(0.8,0.8)
        Box.penup()

        self.SnakeBody.append(Box)

    def Score(self):
        self.score += 1
        self.ScoreT.clear()
        self.ScoreT.write(f"Score: {self.score}",False, "center", ("Arial",15,"normal"))
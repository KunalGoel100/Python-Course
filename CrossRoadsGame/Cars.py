import turtle as T
import random
import Score

class cars:
    def __init__(self):
        temp = T.Turtle()
        temp.speed(10)
        temp.color(random.random(),random.random(),random.random())
        temp.penup()
        temp.shape('square')
        temp.shapesize(1,2)
        temp.setheading(180)
        temp.setposition(350,random.randint(-180,180))
        self.car = temp



class Comp:
    def __init__(self):
        self.CompCars = []
        self.Out = Score.score(2)

    def append(self,car):
        self.CompCars.append(car)

    def move(self,Speed):
        for i in self.CompCars:
            i.forward(Speed)


    def delete(self):
        for i in range(len(self.CompCars)):
            if self.CompCars[i].xcor() <= -380:
                self.CompCars[i].hideturtle()
                self.CompCars.pop(i)
                break

    def collision(self,player):
        for i in self.CompCars:
            if i.distance(player) <= 20:
                self.Out.Out()
                return 0
        return 1


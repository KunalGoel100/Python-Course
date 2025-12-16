import turtle as T
import random
import time

class cars:
    def __init__(self):
        temp = T.Turtle()
        # temp.color([random.randint(0,250),random.randint(0,250),random.randint(0,250)])
        temp.color('white')
        temp.penup()
        temp.shape('square')
        temp.shapesize(1,2)
        temp.setheading(180)
        temp.setposition(350,random.randint(-180,180))
        self.car = temp


class Comp:
    def __init__(self):
        self.CompCars = []

    def append(self,car):
        self.CompCars.append(car)

    def move(self):
        for i in self.CompCars:
            i.forward(40)

    def delete(self):
        for i in range(len(self.CompCars)):
            if self.CompCars[i].xcor() <= -380:
                self.CompCars[i].hideturtle()
                self.CompCars.pop(i)
                break

    def collision(self,player):
        for i in self.CompCars:
            if i.distance(player.pos()) <= 20:
                return 0
        return 1


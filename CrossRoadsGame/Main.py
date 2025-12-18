import time

import Lines
import turtle as T
import Player
import Cars
import random

Screen = T.Screen()
Screen.bgcolor('white')
Screen.screensize(600,600)
Screen.listen()
Screen.tracer(1)

S = [-335, -200]
SS = [-335, 200]
L = Lines.line(S)
L = Lines.line(SS)

Player = Player.player()

gameon = 1
Screen.onkey(Player.Left, 'Left')
Screen.onkey(Player.Right, 'Right')
Screen.onkey(Player.Up, 'Up')

CompCar = Cars.Comp()
Speed = 10
Score = 1
while gameon:
    Screen.tracer(0)
    [Score,speed] = Player.Next()
    Speed += speed
    for i in range(Score):
        chance = random.randint(0,10)
        if chance == 1:
            car = Cars.cars()
            CompCar.append(car.car)



    CompCar.move(Speed)
    time.sleep(0.1)
    Screen.tracer(1)

    CompCar.delete()
    gameon = CompCar.collision(Player.Player)







Screen.exitonclick()
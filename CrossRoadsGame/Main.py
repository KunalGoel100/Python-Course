import Lines
import turtle as T
import Player
import Cars
import time

Screen = T.Screen()
Screen.bgcolor('black')
Screen.screensize(600,600)
Screen.listen()
Screen.colormode(250)

S = [-330, -200]
SS = [-330, 200]
L = Lines.line(S)
L = Lines.line(SS)

Player = Player.player()
Screen.onkey(Player.Left, 'Left')
Screen.onkey(Player.Right, 'Right')
Screen.onkey(Player.Up, 'Up')
gameon = 1


CompCar = Cars.Comp()
while gameon:
    car = Cars.cars()
    CompCar.append(car.car)
    CompCar.move()
    CompCar.delete()
    gameon = CompCar.collision(Player.Player)






Screen.exitonclick()
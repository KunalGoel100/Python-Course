import Lines
import turtle as T
import Player
import Cars

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
Speed = 30
Score = 1
while gameon:
    Screen.tracer(0)
    [Score,speed] = Player.Next()
    Speed += speed
    for i in range(Score):
        car = Cars.cars()
        CompCar.append(car.car)

    Screen.tracer(1)

    CompCar.move(Speed)

    CompCar.delete()
    gameon = CompCar.collision(Player.Player)







Screen.exitonclick()
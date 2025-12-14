import turtle as T
import Ball
import Line
import Colision
import computer

Screen = T.Screen()

Screen.setup(800,800)
Screen.bgcolor('black')
Screen.listen()
Player = Ball.player()
Line = Line.line()
Ball = Ball.ball()
comp = computer.Computer(Ball)
colision = Colision.colision(Ball,Player)

Screen.onkey(Player.Up, 'w')
Screen.onkey(Player.Down, 's')
Screen.onkey(Player.Stop, 'D')

Screen.onkey(comp.Up,'Up')
Screen.onkey(comp.Down,'Down')


Screen.tracer(0)
while Player.gameon:

    Screen.update()

    gameon = colision.out()
    Ball.move()
    Ball.Wall()
    colision.colide()
    comp.CompColide()
    # comp.follow()





Screen.exitonclick()
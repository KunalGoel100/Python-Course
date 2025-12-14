import turtle as T
import Ball
import Player
import Collision
import Objects


Screen = T.Screen()
Screen.setup(500,500)
Screen.bgcolor('black')
Screen.listen()

Ob = Objects.Object()
Ball = Ball.Ball()
GameOn = 1

p = Player.Player()
Screen.onkey(p.Left,'Left')
Screen.onkey(p.Right, 'Right')

Colide = Collision.Collision(p,Ball,Ob)
while GameOn == 1:

    Ball.Move()
    GameOn = Ball.Check()
    Colide.colide()
    Colide.BrickPop()




























Screen.exitonclick()
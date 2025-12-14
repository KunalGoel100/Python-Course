import Lines
import turtle as T
import Player

Screen = T.Screen()
Screen.bgcolor('black')
Screen.screensize(600,600)
Screen.listen()

S = [-330, -200]
SS = [-330, 200]
L = Lines.line(S)
L = Lines.line(SS)

Player = Player.player()
Screen.onkey(Player.Left, 'Left')
Screen.onkey(Player.Right, 'Right')
Screen.onkey(Player.Up, 'Up')






Screen.exitonclick()
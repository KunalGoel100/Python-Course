import turtle as T
import time
import snake

Screen = T.Screen()
Screen.title('Snake Game')
Screen.bgcolor('black')
Screen.setup(500,500)
Screen.tracer(0)

S = snake.Snake()

Screen.listen()
Screen.onkey(S.up, 'Up')
Screen.onkey(S.down, 'Down')
Screen.onkey(S.left, 'Left')
Screen.onkey(S.right, 'Right')

Screen.update()
gameOn = 1
while gameOn == 1:


    time.sleep(0.15)
    S.Move()
    Screen.update()
    gameOn = S.Boundarycheck()
    if gameOn == 1:
        gameOn = S.Selfcheck()

    S.checkFood()

print(f'Final Score: {S.score}')
































Screen.exitonclick()
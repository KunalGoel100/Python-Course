import turtle as T

class Object:
    def __init__(self):
        self.brick = []
        starty = 250
        for i in range(0,5,1):
            startx = -250
            for j in range(0,5,1):
                t = T.Turtle()
                t.penup()
                t.speed(10)
                t.shape('square')
                t.color('white')
                if i%2 == 0:
                    t.goto(startx + 25,starty)
                else:
                    t.goto(startx, starty)
                startx += 50
            starty -= 25
            self.brick.append(t)

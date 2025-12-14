
class Collision:
    def __init__(self,Player,Ball,Object):
        self.Player = Player
        self.Ball = Ball
        self.Object = Object
        pass

    def colide(self):
        # self.Player.Box[i]
        # ballCor = self.Ball.ball.pos()
        for i in range(0,3,1):
            if self.Player.Box[i].distance(self.Ball.ball) <= 10:
                self.Ball.BottomWall()
                break
    def BrickPop(self):
        for i in range(0,len(self.Object.brick),1):
            if self.Object.brick[i].distance(self.Ball.ball) <= 10:
                print("pop")
                self.Object.brick[i].color("black")
                self.Ball.BottomWall()
                del self.Object.brick[i]
                break








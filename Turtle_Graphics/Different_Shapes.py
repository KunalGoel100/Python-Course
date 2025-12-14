from turtle import Turtle as Turtle, Screen
import random

T = Turtle()
T.shape('turtle')
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3,10,1):
    T.color(random.choice(colours))
    for j in range(i):
        T.forward(100)
        T.right(180-((i-2)*180)/i)














screen = Screen()
screen.exitonclick()
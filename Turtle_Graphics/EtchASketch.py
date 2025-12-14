from turtle import Turtle as Turtle, Screen
import turtle
import random
import colorgram

screen = Screen()
screen.colormode(255)
T = Turtle()
screen.listen()
def moveForward():
    T.forward(10)
def moveBack():
    T.back(10)
def turnLeft():
    T.left(10)
def turnRight():
    T.right(10)
def moveSpace():
    T.forward(100)
def home():
    T.penup()
    T.home()
    T.pendown()
def Clear():
    T.clear()
screen.onkeypress(moveForward, 'Up')
screen.onkeypress(moveBack, 'Down')
screen.onkeypress(turnLeft, 'Left')
screen.onkeypress(turnRight, 'Right')
screen.onkey(moveSpace, 'space')
screen.onkeypress(home, 'Home')
screen.onkey(Clear, 'Delete')














screen.exitonclick()
from turtle import Turtle as Turtle, Screen
import turtle
import random
import colorgram

screen = Screen()
screen.setup(width= 500, height= 400)
screen.colormode(255)
T = []
Colour = {1:('Yellow',(242, 238, 0)),
          2:('Red',(255,0,0)),
          3:('Green',(0,255,76)),
          4:('Blue',(0,0,255)),
          5:('LightGreen',(135, 255, 0)),
          6:('LightBlue',(0, 190, 255)),
          7:('Pink',(255, 0, 218)),
          8:('Purple',(147, 0, 255)),
          9:('Orange',(255, 165, 0)),
          10:('Black',(0,0,0))}

for i in range(1,11,1):
    Tim = Turtle()
    T.append(Tim)

print(f'Choose a Turtle:')
for i in range(1,11,1):
    print(Colour[i][0])

UserTurtle = screen.textinput("Turtle","Choose a colour")


# Setting the turtles
for i in range(0,10,1):
    T[i].shape('turtle')
    T[i].penup()
    T[i].color(Colour[i+1][1])
    T[i].goto(-250,150-i*30)

# Doing the race
pos = 0

while pos <= 230:

    for i in range(0,10,1):
        T[i].forward(random.randint(0,10))
    for i in range(0,10,1):
        if T[i].pos()[0] >= pos:
            pos = T[i].pos()[0]
            winner = i+1

if Colour[winner][0] == UserTurtle:
    print("Your Turtle win")
else:
    print("Your Turtle didnt win")
print(f'Winner is Turtle {Colour[winner][0]}')




screen.exitonclick()
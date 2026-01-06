import turtle
import pandas

###################
# Reading The States file
file = pandas.read_csv("50_states_try.csv")

# print(file)
# print(file.state == "Alaska")
###################


screen = turtle.Screen()
screen.addshape("blank_states_img.gif")

Background = turtle.Turtle()
Background.shape("blank_states_img.gif")

tim = turtle.Turtle()
tim.penup()
tim.color("black")



MaxScore = len(file)
score = 0
while len(file) >= 1:
    User = screen.textinput(f"Score {score}/{MaxScore}","Enter State Name")


    if User.title() in file.state.values:
        print("Correct")
        score += 1
        X = int(file.x[file.state == User.title()])
        Y = int(file.y[file.state == User.title()])
        tim.goto(X,Y)
        tim.write(User.title(), False, "center", ("Arial", 10, "normal"))
        file = file[file.state != User.title()]
    else:
        print("Wrong")
print("Game Complete")
screen.exitonclick()
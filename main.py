from turtle import Turtle, Screen
from random import randint
# tam=Turtle()
# my_screen = Screen()
#
# def move_forward():
#     tam.forward(10)
#
# def move_backward():
#     tam.backward(10)
#
# def move_left():
#     tam.left(10)
#
# def move_right():
#     tam.right(10)
# def clear():
#     tam.reset()
#
#
# my_screen.listen()
# my_screen.onkeypress(move_forward,"w")
# my_screen.onkeypress(move_backward,"s")
# my_screen.onkeypress(move_left,"d")
# my_screen.onkeypress(move_right,"a")
# my_screen.onkeypress(clear,"c")



colors=["red","green","purple","yellow","pink","black",]
def generate_turtles():
    turtles=[]
    for i in range (6):
        new_turtle=Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        turtles.append(new_turtle)
    return turtles

def starting_position():
    turtles=generate_turtles()
    x = -230
    y = -150
    for i in range(6):
        turtles[i].teleport(x,y)
        y+=50
    return turtles


is_race_on=False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_choice= my_screen.textinput(title="Make your bet ", prompt="Choose you color of turtle")
if user_choice:
    is_race_on=True
    turtles = starting_position()
while is_race_on:
    for i in range(6):
        turtles[i].forward(randint(0,10))
        if turtles[i].xcor()>=230:
            if turtles[i].pencolor()==user_choice:
                print(f"You have won, Your Turtle won the race")
            else:
                print(f"you have lost, {turtles[i].pencolor()} Turtle won the race")

            is_race_on=False


my_screen.exitonclick()
from turtle import Turtle, Screen 
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which Turtle will win the race? Enter color: ")
colors = ["red", "yellow", "blue", "orange", "green", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        move = random.randint(0,13)
        turtle.forward(move)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won, the {winner} turtle won")
            else:
                print(f"You lost,the {winner} turtle won but    bet on the {user_bet} turtle again")
        




screen.exitonclick()

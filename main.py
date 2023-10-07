from turtle import Turtle, Screen 

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
2

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "b")
screen.onkey(turn_right, "a")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "p")
screen.onkey(clear, "c")
screen.exitonclick()
import turtle
screen=turtle.Screen()
screen.bgcolor("white")
pen=turtle.Turtle()
pen.color("blue")
pen.speed(3)
for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.hideturtle()
screen.exitonclick()
import random
from turtle import Turtle, Screen


color_list = [(249, 212, 93), (150, 69, 97), (53, 99, 155), (232, 137, 62), (107, 174, 211), (243, 237, 241), (114, 83, 59), (201, 146, 177), (200, 77, 109), (145, 134, 72), (230, 90, 59), (141, 192, 140), (72, 103, 90), (68, 162, 92), (5, 165, 179), (227, 161, 183), (115, 126, 142), (163, 196, 221), (16, 66, 123), (187, 24, 34), (13, 56, 103), (235, 172, 160), (175, 201, 179), (163, 200, 215), (186, 27, 25), (80, 55, 37), (96, 61, 30)]


screen = Screen()
screen.colormode(255)

# Turtle setup
paint = Turtle()
paint.up()
paint.speed("fastest")
paint.hideturtle()
# Initial position
paint.setheading(225)
paint.forward(300)
paint.setheading(0)
x_position = paint.xcor()
y_position = paint.ycor()

# Painting
for y in range(10):
    paint.setx(x_position)
    paint.sety(y_position + y * 50)
    for x in range(10):
        paint.dot(20, random.choice(color_list))
        paint.forward(50)


screen.exitonclick()

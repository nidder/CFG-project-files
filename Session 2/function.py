import turtle
def triangle(side_length, colour):
    angle = 120
    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()

triangle(100,'green')
triangle(50,'blue')
turtle.done


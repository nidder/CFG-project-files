import turtle
sides= int(input('number of sides: '))
angle= 360 / sides
side_length= 60

for side in range (sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done()
for number in range(100):
   output= 'o'*number
print(output)

def calculate_vat(amount):
    amount*1.2
    return amount * 1.2
total= calculate_vat (100)
print(total)


import turtle

def triangle(colour):
    triangle_side = 200
    triangle_angle = 120

    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(3):

        turtle.forward(triangle_side)
        turtle.left(triangle_angle)

triangle('green')
turtle.end_fill()

def square(square_side,square_colour):
    square_angle = 90

    turtle.color(square_colour,square_colour)
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(square_side)
        turtle.right(square_angle)
    turtle.end_fill()


square(200,'yellow')
turtle.forward(25)
turtle.penup()
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.pendown()
square(50,'purple')
turtle.left(90)
turtle.penup()
turtle.forward(40)
turtle.pendown()
square(50,'purple')
turtle.penup()
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
square(50,'purple')
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.right(270)
turtle.pendown()
square(50,'purple')
turtle.penup()
turtle.forward(80)
turtle.pendown()
turtle.right(270)
turtle.forward(10)
turtle.right(270)
turtle.forward(70)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(70)
turtle.right(270)
turtle.forward(10)
turtle.done()



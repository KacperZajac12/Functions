import turtle
from turtle import pen
    
def draw_square(length):

    # Side length
    side_length = length

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)



def draw_triangle(length):


    # Side length
    side_length = length

    # Draw a square
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)


def draw_rectangle(length_a, length_b):



    # Side length
    side_length = length_a
    side_length2 = length_b

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        if i % 2 == 0:
            pen.forward(side_length2)
        pen.right(90)

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle 
pen = turtle.Turtle()
pen.speed(5)

draw_square(100)

pen.penup()
pen.goto(-200,100)

pen.pendown()
draw_rectangle(100,50)

pen.penup()
pen.goto(300,100)

pen.pendown()
draw_triangle(100)

    # Hide the turtle and finish
pen.hideturtle()
window.mainloop()
import turtle
def draw_square(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = length

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_triangle(length):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = length

    # Draw a square
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

def draw_rectangle(length_a, length_b):
    # Set up the screen
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = length_a
    side_length2 = length_b

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        if i % 2 == 0:
            pen.forward(side_length2)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()

import turtle

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100

# Draw a square
for i in range(3):
    pen.forward(side_length)
    pen.right(120)

# Hide the turtle and finish
draw_square(50)
pen.hideturtle()
window.mainloop()
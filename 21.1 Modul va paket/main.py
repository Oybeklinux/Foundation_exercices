import turtle
import math

# Set up the screen and turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Set up the coordinate system
screen.setworldcoordinates(-10, -10, 10, 10)

# Set up the turtle
t.speed(0)  # Set the maximum speed
t.penup()
t.goto(-10, 0)
t.pendown()

# Draw the cardioid (heart-shaped curve)
t.color("red")  # Set the color to red
scale_factor = 0.5
t.begin_fill()
t.fillcolor("red")
for angle in range(0, 360):
    theta = math.radians(angle)
    x = scale_factor * 16 * (math.sin(theta) ** 3)
    y = scale_factor * 13 * math.cos(theta) - scale_factor * 5 * math.cos(2 * theta) - scale_factor * 2 * math.cos(3 * theta) - scale_factor * math.cos(4 * theta)
    t.goto(x, y)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until manually closed
screen.mainloop()

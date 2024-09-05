# A program that draws a series of colourful fireworks

# ----------------
# Import libraries
# ----------------

import turtle
import random

# ----------------
# Subprograms
# ----------------
colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

def draw_fireworks():
    for i in range(10):
        colour = random.choice(colours)
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        draw_firework_burst(x, y, colour)

def draw_firework_burst(x, y, colour):
    tim.penup()
    tim.setposition(x, y)
    tim.pendown()
    tim.pencolor(colour)
    length = random.randint(75, 150)
    for i in range(12):
        tim.forward(length)
        tim.backward(length)
        tim.right(30)


# ----------------
# Main program
# ----------------

tim = turtle.Turtle()
turtle.bgcolor("black")
tim.hideturtle()

draw_fireworks()

turtle.done()
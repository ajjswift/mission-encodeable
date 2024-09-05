# A program that draws the German flag

# ----------------
# Import libraries
# ----------------

import turtle

# ----------------
# Subprograms
# ----------------

def draw_rectangle(colour, width, height):
    tim.begin_fill()
    tim.fillcolor(colour)
    for i in range(2):
        tim.forward(width)
        tim.right(90)
        tim.forward(height)
        tim.right(90)
    tim.end_fill()

def draw_german_flag():
    tim.penup()
    tim.goto(-200, 100)
    tim.pendown()
    draw_rectangle("#000000", 400, 100)
    tim.penup()
    tim.goto(-200, 0)
    tim.pendown()
    draw_rectangle("#FF0000", 400, 100)
    tim.penup()
    tim.goto(-200, -100)
    tim.pendown()
    draw_rectangle("#FFCC00", 400, 100)
    tim.hideturtle()
    turtle.done()

# ----------------
# Main program
# ----------------

tim = turtle.Turtle()
draw_german_flag()

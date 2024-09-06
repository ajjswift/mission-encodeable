# A program where turtles race each other

# ----------------
# Import libraries
# ----------------

import turtle
import random

# ----------------
# Subprograms
# ----------------

def set_up_background():
    turtle.bgcolor("black")
    helper_turtle = turtle.Turtle()
    helper_turtle.begin_fill()
    helper_turtle.fillcolor("gold")
    helper_turtle.hideturtle()
    helper_turtle.circle(20)
    helper_turtle.end_fill()

def set_up_turtle(colour, y):
    new_turtle = turtle.Turtle()
    new_turtle.shape("circle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.setposition(0, y)
    new_turtle.pendown()
    return new_turtle



# ----------------
# Main program
# ----------------

set_up_background()


mercury = set_up_turtle('light grey', -60)
venus = set_up_turtle('yellow', -100)
earth = set_up_turtle('blue', -140)
mars = set_up_turtle('red', -180)


winner = False
total_mars_extent = 0
total_earth_extent = 0
total_venus_extent = 0
total_mercury_extent = 0

while not winner:
    mars_extent = random.randint(5, 10)
    earth_extent = random.randint(5, 10)
    venus_extent = random.randint(5, 10)
    mercury_extent = random.randint(5, 10)
    mars.circle(200, extent=mars_extent)
    earth.circle(160, extent=earth_extent)
    venus.circle(120, extent=venus_extent)
    mercury.circle(80, extent=mercury_extent)
    total_mars_extent += mars_extent
    total_earth_extent += earth_extent
    total_venus_extent += venus_extent
    total_mercury_extent += mercury_extent
    if total_mars_extent >= 360:
        winner = True
        mars.write('    Mars wins!', font=('Arial', 16, 'normal'))

    if total_earth_extent >= 360:
            winner = True
            earth.write('    Earth wins!', font=('Arial', 16, 'normal'))

    if total_venus_extent >= 360:
            winner = True
            venus.write('    Venus wins!', font=('Arial', 16, 'normal'))

    if total_mercury_extent >= 360:
            winner = True
            mercury.write( '    Mercury wins!', font=('Arial', 16, 'normal'))


turtle.done()
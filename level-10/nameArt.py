# A program that draws my name 

# ----------------
# Import libraries
# ----------------
import turtle

# ----------------
# Subprograms
# ----------------
def draw_name():
    # Letter A
    tim.up()
    tim.backward(180)
    tim.left(70)
    tim.down()
    tim.forward(100)
    tim.right(140)
    tim.forward(100)
    tim.up()
    tim.backward(40)
    tim.right(110)
    tim.down()
    tim.forward(41.04)
    tim.up()
    tim.backward(41.04)
    tim.left(110)
    tim.forward(40)
    tim.left(70)

    # Letter L
    tim.up()
    tim.forward(30)
    tim.left(90)
    tim.down()
    tim.forward(95)
    tim.up()
    tim.right(180)
    tim.forward(95)
    tim.down()
    tim.left(90)
    tim.forward(50)
    
    # Letter E
    tim.up()
    tim.forward(30)
    tim.down()
    tim.forward(50)
    tim.up()
    tim.left(180)
    tim.forward(50)
    tim.right(90)
    tim.down()
    tim.forward(47.5)
    tim.right(90)
    tim.forward(50)
    tim.up()
    tim.right(180)
    tim.forward(50)
    tim.right(90)
    tim.down()
    tim.forward(47.5)
    tim.right(90)
    tim.forward(50)
    tim.up()
    tim.right(90)
    tim.forward(95)
    tim.left(90)

    # Letter X
    tim.forward(30)
    tim.down()
    tim.left(65)
    tim.forward(100)
    tim.up()
    tim.left(115)
    tim.forward(40)
    tim.left(115)
    tim.down()
    tim.forward(100)



# ----------------
# Main program
# ----------------
global tim
tim = turtle.Turtle()
draw_name()
turtle.done()
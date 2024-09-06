# A program which draws a portrait

# ----------------
# Import libraries
# ----------------

import turtle

# ----------------
# Subprograms
# ----------------



# ----------------
# Main program
# ----------------

tim = turtle.Turtle()
tim.speed(100000000)
tim.left(90)
tim.up()
tim.forward(70)
tim.down()
tim.forward(30)
for i in range(90):
    tim.forward(2)
    tim.left(1)

for i in range(95):
    tim.forward(0.8)
    tim.left(1)

tim.forward(70)

for i in range(5):
    tim.forward(8)
    tim.right(1)

tim.forward(80)
for i in range(20):
    tim.forward(2)
    if i % 2 == 0:
        tim.left(10)
    else:
        tim.right(10)

tim.forward(20)

for i in range(90):
    tim.forward(0.65)
    tim.left(1)

tim.forward(125)

for i in range(180):
    tim.forward(0.35)
    tim.left(1)

tim.right(4)
tim.forward(12)

for i in range(88):
    tim.forward(0.15)
    tim.right(2)

tim.forward(12)


for i in range(180):
    tim.forward(0.35)
    tim.left(1)

tim.forward(10)

for i in range(90):
    tim.right(1)
    tim.forward(0.1)

tim.forward(30)

for i in range(90):
    tim.right(1)
    tim.forward(0.05)

tim.forward(34)

for i in range(127):
    tim.left(1)
    tim.forward(0.1)

tim.forward(73)

tim.position(150, -75)

#turtle.done()
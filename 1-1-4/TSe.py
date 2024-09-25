#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors
num_lines = 5
color1 = "green"
color2 = "red"
color3 = "blue"

wn = trtl.Screen()
height = 90  # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 1
angle = 160  # experiment with the shape
seg = int(360 / angle)

while (painter.ycor() < height):
    if (space % 2 == 0):
        painter.fillcolor(color1)
        painter.color(color1)
    elif (space % 2 == 1):
        painter.fillcolor(color2)
        painter.color(color2)
    elif (space % 5 == 4):
        painter.fillcolor(color3)
        painter.color(color3)

    painter.right(angle)
    painter.forward(4 * space + 10)  # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space += 1

wn.mainloop()
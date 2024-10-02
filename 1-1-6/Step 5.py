#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legs = 8
leg_length = 70
angle = 360 / legs
painter.pensize(5)
leg_distance = 0
while (leg_distance < legs):
  painter.goto(0,20)
  painter.setheading(angle*leg_distance)
  painter.forward(leg_length)
  leg_distance = leg_distance + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
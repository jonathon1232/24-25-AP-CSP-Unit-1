import turtle as trtl

painter = trtl.Turtle()

painter.forward(-100)
painter.right(-90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)

painter.penup()
painter.goto(-100,0)
wn = trtl.Screen()
wn.mainloop()
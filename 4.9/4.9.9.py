import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Screen.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

def csillag():
    for i in range(0,5):
        Teknos.right(144)
        Teknos.forward(100)
Teknos.right(144)
csillag()
Screen.mainloop()
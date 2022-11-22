import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.left(90)
Screen.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

Teknos.left(90)
def kor(r):
    for i in range(0,36):
        Teknos.forward(r)
        Teknos.right(10)

kor(30)
Screen.mainloop()
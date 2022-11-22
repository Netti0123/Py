import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()

class rajzol:
    def nyolcszog(szog, elore, sz):
        for i in range(0,sz):
            Teknos.forward(elore)
            Teknos.left(szog)
            Teknos.forward(elore)

Screen.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

rajzol.nyolcszog(60,50,6)
Teknos.back(50)
Screen.mainloop()
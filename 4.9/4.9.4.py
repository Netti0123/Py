import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Teknos.left(90)
Screen.bgcolor("lightgreen")
Teknos.color("pink")
Teknos.pensize(3)

class rajzol:
    def negyzet(elore,szog,szor):
            for x in range(0, szor):
                Teknos.speed(10)
                Teknos.right(15)
                for i in range(0, 4):
                    Teknos.forward(elore)
                    Teknos.right(szog)

rajzol.negyzet(100,90,24)
Screen.mainloop()
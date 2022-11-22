import turtle
Screen = turtle.Screen()
Teknos = turtle.Turtle()
Screen.bgcolor("lightgreen")
Teknos.color("blue")
Teknos.pensize(1)
Teknos.speed(10)

class rajzol:
    def csiga(elore, szog, szor):
        for i in range(0,szor):
            Teknos.forward(elore +(i+i))
            Teknos.left(szog)

rajzol.csiga(10,90,147)
Screen.mainloop()
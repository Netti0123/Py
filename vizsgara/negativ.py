x= int(input("Adj meg egy számot!"))
y= int(input("Add meg a második számot!: "))

def szamok():
    if x < 0:
        print("Az első szám negatív!")

    elif y < 0:
        print("Az második szám negatív!")

    elif x < 0 and y< 0:
        print("Mind a két szám negatív")
    else:
        print("Egyik sem negativ")

szamok()
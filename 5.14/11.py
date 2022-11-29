a = int(input("Elso oldal:"))
b = int(input("Masodik oldal:"))
c = int(input("Harmadik oldal(a legnagyobb):"))

def derekszogu_e():
    if (a**2)+(b**2)==(c**2):
        print("derékszögű")
    else:
        print("nem derékszögű")

derekszogu_e()
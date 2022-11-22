x=int(input("A: "))
y=int(input("B: "))
if x<0 and y<0:
    print("Mindkét szám negatív")
elif x>0 and y>0:
    print("Mindkét szám pozitiv")
elif x<0:
    print("Az első szám negatív")
elif y<0:
    print("Az második szám negatív")
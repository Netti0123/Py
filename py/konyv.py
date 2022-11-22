def long(a):
    b=False
    if a>15:
        b=True
    return b

cim=input("cím: ")

while(cim!=""):
    oldal=int(input("oldalak: "))
    old=long(oldal)
    if old:
        print("A könyv hosszú")
    else:
        print("A könyv rövid")
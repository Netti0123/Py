def magasE(mag):
    if mag > 170:
        return True
    else:
        return False

nev =input("Nev:")
while(nev!=""):
    m=int(input("Magassag:"))
    if magasE(m):
        print(nev, "Magasabb mint az atlag")
    else:
        print(nev, "Nem magasabb mint az atlag")
nev=input("Nev:")
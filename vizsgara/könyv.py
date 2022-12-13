cim = input("Add meg a konyv cimet!: ")
oldal = int(input("Add meg az oldaolak szamat! "))
a = "A", cim, "hosszu a konyv"
b = "A", cim, "rovid terjedelmu"
def konyvek():

    if oldal > 150:
        print(a)
    else:
        print(b) 
        
while cim == "":
    cim = input("Add meg a konyv cimet!: ")
    oldal = int(input("Add meg az oldaolak szamat! "))
print(konyvek())
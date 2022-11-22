#tömbös progi
#t=[1,2,5,7,"jolán"]
#print(t)
import random

#t=[]
#for x in range(5):
#    t.append(int (input("Adj egy számot")))
#print(t)

t=[]
for x in range(5):
    t.append(random.randint(1,100))
print(t)
#összegzes tetel
osszeg=0
for x in t:
    osszeg+=x
print(osszeg)

#atlag szamitas tetele
atl=osszeg/len(t)
print(atl)

#min
min=101
for x in t:
    if min>x:
        min=x
print(min)

#max
max=-1
for x in t:
    if max<x:
        max=x
print(max)

#keresés




import random
while(os!=2):
    a =random.randint(1,100)
    print("A szam",a)
    os = 0

for x in range(1,a+1):
    if a%x==0:
        os+=1
if os==2:
    print("Prím",os,"osztoja van!")
else:
    print("Nem prím",os,"osztoja van!")
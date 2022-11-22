xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def jegy():
    for x in xs:
        if x<60:
            print("Ulj le egyes: ")

        if x>=60 and x<71:
            print("Kettes: ")

        if x>=70 and x<81:
            print("Hármas: ")
            
        if x>=80 and x<91:
            print("Negyes: ")

        if x>90:
            print("otos: ")
jegy()
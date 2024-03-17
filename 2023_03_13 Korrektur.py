# Aufgabe 1

def größte(zahl1, zahl2, zahl3): 
    if zahl1 > zahl2 and zahl1 > zahl3:
        print(zahl1)
    elif zahl2 > zahl1 and zahl2 > zahl3:
        print(zahl2)
    else:
        print(zahl3)

# Aufgabe 2 

def summe_oder_product(zahl1, zahl2):
    if zahl1 + zahl2 > zahl1 * zahl2:
        print(zahl1 + zahl2)
    else:
        print(zahl1 * zahl2)
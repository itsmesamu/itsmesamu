def hallo():
    print("hallo") 
    hallo()
hallo()



def hallo_n(n):
    if n == 0:
        return
    print("Hallo")
    hallo_n(n - 1)
hallo_n(10)

import random
def n_zufallszahl_ausgabe(n):
    if n == 0:
        return
    zufallszahl = random.randint(-50, 50)
    print(zufallszahl)
    n_zufallszahl_ausgabe(n - 1)

def n_bis_eins(n):
    if n == 0:
        return
    print(n)
    n_bis_eins(n - 1)
n_bis_eins(5)
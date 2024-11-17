def gleicher_betrag(zahl1: int, zahl2:int) -> bool:
    if zahl1 == zahl2:
        return True
    elif -zahl1 ==zahl2:
        return True
    elif zahl1 == -zahl2:
        return  True
    else:
        return False
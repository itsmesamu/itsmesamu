def listensumme_positiv(liste: list) -> int:
     i = 0
     summe = 0
     while i < len (liste):
        if liste[i] > 0:
            summe+=liste[i]
        i += 1 
     return summe

def listensumme_positiv_alt(liste: list) -> int:
   summe = 0
   for i in  range (len(liste)):
       if liste[i] > 0:
           summe += liste[i]
   return summe

def listensumme_positiv_alt_alt(liste: list) -> int:
    summe = 0 
    for zahl in liste:
        if zahl > 0:
            summe += zahl
    return summe

def listensumme_positiv_alt_alt_alt(liste: list) -> int:
    return sum([list for zahl in liste if zahl > 0])
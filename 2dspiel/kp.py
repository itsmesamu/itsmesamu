import random

# Die Karten der verschiedenen Wertungen
karten = ["Ass", "King", "Queen", "Jack", "10", "9", "8", "7"]

 # Erstelle leere Liste, um alle möglichen Kombinationen zu speichern
kombi_liste = []
for i in range(len(karten) ** 2):
        kombi_liste.append([])
    
# Füllen Sie die Kombinationsliste mit allen möglichen Kombinationen
def fill_combis():
        for i in range(len(karten)):
            for j in range(i+1, len(karten)):
                kombi_liste[i*j].append((karten[i], karten[j]))
            
fill_combis()

# Wähle zufällig eine Kombination aus
wahl = kombi_liste[random.randint(0, len(kombi_liste)-1)]

# Zeigt die Ergebnisse an    
print("Du hast folgende Karten ausgewählt:")
for karte in wahl:
        print(karte[0] + " of " + karte[1]):
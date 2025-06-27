def doppelte_buchstaben(Hallo: str) -> int:
    count = 0
    i = 0
    while i < len(Hallo) - 1:
        if Hallo[i] == Hallo[i + 1]:
            count += 1
            # Überspringe die gesamte Gruppe gleicher Buchstaben
            while i < len(Hallo) - 1 and Hallo[i] == Hallo[i + 1]:
                i += 1
        i += 1
    return count
print(doppelte_buchstaben("korrektur"))        

L = [8, 24,48,2,16]
def liste():
    compteur = 0
    for i in (L):
        if i % 3 == 0:
            compteur += 1
    return compteur
print(liste())


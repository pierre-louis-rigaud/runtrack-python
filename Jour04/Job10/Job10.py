L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def somme() :
    compteur = 1
    for i in L:
        if i <= 90 and i >= 25 :
            compteur *= i
    return compteur
print("Le produit de toutes les valeurs de la liste de 25 à 90 est:",somme())
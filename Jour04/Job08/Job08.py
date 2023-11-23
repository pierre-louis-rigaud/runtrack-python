L =[8,24,27,48,2,16,9,7,84,91]
def somme() :
    compteur = 0
    for i in L:
        if i%2 == 0 :
            compteur += i
    return compteur
print(somme())
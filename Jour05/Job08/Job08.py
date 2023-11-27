def test_tri(liste):
    count = 0
    i = 1
    number_loop = 0 
    while i < len(liste):
        number_loop += 1
        if liste[i] < liste[i-1]:
            liste[i], liste[i-1] = liste[i-1], liste[i]
            count += 1
        i += 1

    if count > 0:
        return 1 ,count, number_loop
    else:
        return 0, count, number_loop
        
    
def tri(liste):
    finish_count = 1
    total_count = 0
    total_loops = 0
    while finish_count != 0 :
        finish_count -= 1
        finish_count, moves_count, number_loop = test_tri(liste)
        total_count += moves_count
        total_loops += number_loop
    print(f"Nombre de total de coups nécessaires pour trier la liste : {total_count}")
    print(f"Nombre total de boucles : {total_loops}")
    return liste

L4= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L3 = [64, 34, 25, 12, 22, 11, 90]
L = [1,2,3,5,4,6,7,8,9,10,11,12,13,14,15]
print("\n----------Résultats de ma version du tri à bulles----------\n")
print(f"Liste triée : {tri(L)}\n")

def tri_bulles(tableau):
    n = len(tableau)
    coups = 0
    boucles = 0

    for i in range(n):
        for j in range(0, n-i-1):
            boucles += 1
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                coups += 1

    return tableau, coups, boucles

L4= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
L3 = [64, 34, 25, 12, 22, 11, 90]
L = [1,2,3,5,4,6,7,8,9,10,11,12,13,14,15]
tri, nombre_coups, nombre_boucles = tri_bulles(L)
print("----------Résultats du tri à bulles trouvé sur internet----------\n")
print("Tableau trié:", tri)
print("Nombre de coups pour le tri à bulles:", nombre_coups)
print("Nombre total de boucles parcourues:", nombre_boucles, "\n")

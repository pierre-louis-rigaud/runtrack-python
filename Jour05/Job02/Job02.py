def dessiner_rectangle(longueur, largeur):
    print("|" + "-" * (longueur - 2) + "|")

    for i in range(largeur - 2):
        print("|" + " " * (longueur - 2) + "|")

    print("|" + "-" * (longueur - 2) + "|")
dessiner_rectangle(10, 3)
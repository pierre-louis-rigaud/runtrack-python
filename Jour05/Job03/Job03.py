def triangle(hauteur):
    for i in range(0,hauteur):
        espace = hauteur - i
        if i == hauteur -1:
            ligne = "/" + "_" * (hauteur * 2 - 2) + "\\"
        elif i == 0:
            ligne = " " * (hauteur - 1) + "/" + "\\"
        else:
            ligne = " " * (hauteur - i -1) + "/" + " " * (i * 2) + "\\"
        print(ligne)
triangle(10)